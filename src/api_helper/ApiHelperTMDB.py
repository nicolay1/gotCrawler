from urllib.parse import urljoin
from typing import Dict

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
        raise NotImplementedError
