from typing import Dict
from src.models.Episode import Episode
from src.models.Author import Author
from src.models.Actor import Actor

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
        return self._get("trending/tv/week", None, {"page":page})

    def get_show(self, show_id: int):
        return self._get("tv/{}", (show_id))

    def get_season(self, show_id: int, season_number: int):
        return self._get("tv/{}/season/{}", (show_id, season_number))

    def get_episode(self, show_id: int, season_number: int, episode_number: int):
        return self._get("tv/{}/season/{}/episode/{}", (show_id, season_number, episode_number))

    def _api_json_to_show(self, show_json: Dict):
        raise NotImplementedError

    def _api_json_to_season(self, season_json: Dict):
        raise NotImplementedError

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
