from src.api_helper.ApiHelperTMDB import ApiHelperTMDB


class SeasonController:
    """
        This controller manages the season model
    """

    @classmethod
    def get_one_season(cls, show_id: int, num_season: int):
        api = ApiHelperTMDB()
        return api.get_season(show_id, num_season)
