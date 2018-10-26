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
        json= self._get("tv/{}", (show_id))
        self._api_json_to_show(json)

    def get_season(self, show_id: int, season_number: int):
        json = self._get("tv/{}/season/{}", (show_id, season_number))
        self._api_json_to_season(json, show_id)

    def get_episode(self, show_id: int, season_number: int, episode_number: int):
        return self._get("tv/{}/season/{}/episode/{}", (show_id, season_number, episode_number))

    def _api_json_to_show(self, show_json: Dict):
        title = show_json["original_name"]
        pict = show_json["poster_path"]
        api_id = show_json["id"]
        season_next_episode_num = show_json["next_episode_to_air"]["season_number"]
        next_episode_num = show_json["next_episode_to_air"]["episode_number"]
        date_next_episode = show_json["next_episode_to_air"]["air_date"]
        last_maj = datetime.now()
        db_id = None
        season_list = []
        for season_number in show_json["seasons"]:
            season_list.append(self._api_json_to_season(self.get_season(api_id, season_number), api_id))
        number_of_episodes = show_json["number_of_episodes"]
        number_of_seasons = show_json["number_of_seasons"]

        show = Show(title, pict, api_id, season_next_episode_num, next_episode_num, date_next_episode,
                    last_maj, db_id, season_list, number_of_episodes, number_of_seasons)
        return show

    def _api_json_to_season(self, season_json: Dict, id_show: int):
        name = season_json["name"]
        overview = season_json["overview"]
        poster = season_json["poster_path"]
        num_season = season_json["season_number"]
        list_episodes = []
        for json in season_json["episodes"]:
            list_episodes.append(self._api_json_to_episode(json))
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
