from flask_restful import Resource

from src.controllers.SeasonController import SeasonController
from src.errors import ErrorSeasonDoesNotExist

class SeasonGet(Resource):
    """
        Get a season of a show
    """
    def get(self, show_api_id, num_season):
        try:
            season = SeasonController.get_one_season(show_api_id, num_season)
        except ErrorSeasonDoesNotExist:
            return ErrorSeasonDoesNotExist.flask_desc_code()
        return season.to_json()
