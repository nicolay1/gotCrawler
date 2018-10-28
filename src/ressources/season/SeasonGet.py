from flask_restful import Resource

from src.controllers.SeasonController import SeasonController


class SeasonGet(Resource):
    """
        Get a season of a show
    """
    def get(self, show_api_id, num_season):
        season = SeasonController.get_one_season(show_api_id, num_season)
        return season.to_json()
