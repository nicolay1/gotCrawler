from src.models.Episode import *

from src.api_helper import ApiHelperTMDB


class EpisodeController:

    """
        This controller manage the episode model
    """

    @classmethod
    def get_one_ep(cls, show_id: int, num_season: int, num_ep: int):
        return ApiHelperTMDB().get_episode(show_id, num_season, num_ep)
