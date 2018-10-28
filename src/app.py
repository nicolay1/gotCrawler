from flask import Flask
from flask_restful import Resource, Api

from src.ressources import UserGet, UserAdd, UserGetPref

class GotCrawlerApp:
    """
        This is the flask app 
    """
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)

    def _initialize(self):
        self.api.add_resource(UserGet, '/user/<user_id>')
        self.api.add_resource(UserAdd, '/user')
        self.api.add_resource(UserGetPref, '/user/<user_id>/pref')

    def start(self):
        self._initialize()
        self.app.run(debug=1)
