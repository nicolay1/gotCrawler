from typing import Dict
from src.models.Show import *
from datetime import datetime
from src.models.Episode import Episode
from src.models.Author import Author
from src.models.Actor import Actor
from src.models.Season import Season
from src.config import CONFIG
from src.api_helper.ApiHelper import ApiHelper


class ApiHelperTMDB(ApiHelper):
    """
        TMDB Api Caller
    """

    def __init__(self):
        super().__init__(
            CONFIG["tmdb_api_root"],
            {
                "api_key": CONFIG["tmdb_api_key"]
            }
        )

    def get_trending(self, page=1):
        return self._get("trending/tv/week", None, {"page": page})

    def get_show(self, show_id: int):
        json = self._get("tv/{}", (show_id))
        return self._api_json_to_show(json)

    def get_season(self, show_id: int, season_number: int):
        json = self._get("tv/{}/season/{}", (show_id, season_number))
        return self._api_json_to_season(json, show_id)

    def get_episode(self, show_id: int, season_number: int, episode_number: int):
        json = self._get("tv/{}/season/{}/episode/{}", (show_id, season_number, episode_number))
        return self._api_json_to_episode(json)

    def get_search(self, query: str):
        json = self._get("search/tv", None, {"query": query})
        return self._api_json_search_to_show_list()

    def _api_json_search_to_show_list(self, result_json: Dict):
        show_list = []
        for show_json in result_json["results"]:
            title = show_json["name"]
            pict = show_json["poster_path"]
            api_id = show_json["id"]
            overview = show_json["overview"]
            show = Show(title=title, pict=pict, api_id=api_id, season_next_episode_num=None,
                        next_episode_num=None, date_next_episode=None,
                        last_maj=datetime.now(), db_id=None, season_list=None, number_of_episodes=None,
                        number_of_seasons=None, overview=overview)
            show_list.append(show)
        return show_list

    def _api_json_to_show(self, show_json: Dict):
        title = show_json["name"]
        pict = show_json["poster_path"]
        api_id = show_json["id"]
        season_next_episode_num = show_json["next_episode_to_air"]["season_number"]
        next_episode_num = show_json["next_episode_to_air"]["episode_number"]
        date_next_episode = show_json["next_episode_to_air"]["air_date"]
        last_maj = datetime.now()
        db_id = None
        number_of_episodes = show_json["number_of_episodes"]
        number_of_seasons = show_json["number_of_seasons"]
        overview = show_json["overview"]
        list_season = []
        for season_json in show_json["seasons"]:
            num_season = season_json["season_number"]
            name = season_json["name"]
            overview = season_json["overview"]
            poster = season_json["poster_path"]
            season = Season(api_id, num_season, name, poster, overview, None)
            list_season.append(season)

        show = Show(title=title, pict=pict, api_id=api_id, season_next_episode_num=season_next_episode_num,
                    next_episode_num=next_episode_num, date_next_episode=date_next_episode,
                    last_maj=last_maj, db_id=db_id, season_list=list_season, number_of_episodes=number_of_episodes,
                    number_of_seasons=number_of_seasons, overview=overview)
        return show

    def _api_json_to_season(self, season_json: Dict, id_show: int):
        name = season_json["name"]
        overview = season_json["overview"]
        poster = season_json["poster_path"]
        num_season = season_json["season_number"]
        list_episodes = []
        for episode_json in season_json["episodes"]:
            list_episodes.append(self._api_json_to_episode(episode_json))
        return Season(id_show=id_show, num_season=num_season, list_episodes=list_episodes, name=name, poster=poster,
                      overview=overview)

    def _api_json_to_episode(self, episode_json: Dict):
        name = episode_json["name"]
        num_season = episode_json["season_number"]
        num_ep = episode_json["episode_number"]
        summary = episode_json["overview"]
        list_actor = [
            self._api_json_to_actor(actor_json) for actor_json in episode_json["guest_stars"]
        ]
        list_author = [
            self._api_json_to_author(author_json) for author_json in episode_json["author_json"]
        ]
        return Episode(name, num_season, num_ep, summary, list_actor, list_author)

    @staticmethod
    def _api_json_to_author(author_json: Dict):
        name = author_json["name"]
        role = "{}: {}".format(author_json["department"], author_json["job"])
        return Author(name, role)

    @staticmethod
    def _api_json_to_actor(actor_json: Dict):
        name = actor_json["name"]
        pict = actor_json["profile_path"]
        return Actor(name, pict)
