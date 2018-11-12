from flask import Flask

from flask_restful import Resource, Api
from flask_cors import CORS

from src.ressources import UserGet, UserAdd, UserPref, UserPrefDelPut, SeasonGet, EpisodeGet, ShowGet, ShowSearch, AuthUser, AuthRenew
from src.ressources.show import ShowTrending

from src.notification_manager.NotificationManager import NotificationManager

class GotCrawlerApp:
    """
        This is the flask app 
    """
    def __init__(self):
        self.app = Flask(__name__)
        CORS(self.app)
        self.api = Api(self.app)
        NotificationManager().start()

    def _initialize(self):
        # post : login,pwd
        self.api.add_resource(AuthUser, '/auth')
        # get : Bearer Token Jwt
        self.api.add_resource(AuthRenew, '/auth/renew')

        # all routes but UserAdd need the jwt token of user_id
        # get
        self.api.add_resource(UserGet, '/user/<user_id>')
        # post : poster, firstname, lastname, login, password
        self.api.add_resource(UserAdd, '/user')
        # post : show_id (add pref with show_id for user_id), get : get all user pref
        self.api.add_resource(UserPref, '/user/<user_id>/pref')
        # delete : (delete), put : seen_flag (change the seen_flag of the user)
        self.api.add_resource(UserPrefDelPut, '/user/<user_id>/pref/<show_id>')

        # get: show by it's id
        self.api.add_resource(ShowGet, '/show/<api_id>')
        # get: param : q, search for a show
        self.api.add_resource(ShowSearch, '/show/search')
        # get, search for trending
        self.api.add_resource(ShowTrending, '/show/trending')
        # get : seqrch for season/episode
        self.api.add_resource(SeasonGet, '/show/<show_api_id>/season/<num_season>')
        self.api.add_resource(EpisodeGet, '/show/<show_api_id>/season/<num_season>/episode/<num_episode>')

    def start(self):
        self._initialize()
        self.app.run(debug=1)
