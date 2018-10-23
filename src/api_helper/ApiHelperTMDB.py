from urllib.parse import urljoin
from typing import Dict
from src.models.Show import *
from datetime import datetime

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
        json= self._get("tv/{}", (show_id))
        self._api_json_to_show(json)

    def get_season(self, show_id: int, season_number: int):
        return self._get("tv/{}/season/{}", (show_id, season_number))

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

    def _api_json_to_season(self, season_json: Dict):
        raise NotImplementedError

    def _api_json_to_episode(self, episode_json: Dict):
        raise NotImplementedError
