from flask_restful import Resource

from src.controllers.EpisodeController import EpisodeController

from src.errors import ErrorEpisodeDoesNotExist

class EpisodeGet(Resource):
    """
        Get an episode of a season of a show
    """
    def get(self, show_api_id, num_season, num_episode):
        try:
            episode = EpisodeController.get_one_ep(show_api_id, num_season, num_episode)
        except ErrorEpisodeDoesNotExist:
            return ErrorEpisodeDoesNotExist.flask_desc_code()
        return episode.to_json()
