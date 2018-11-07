from flask import request

from src.controllers.UserController import UserController
from src.db.MyDBConnection import MyDBConnection

from .User import UserRessource

class UserGet(UserRessource):
    """
        Get a user
    """

    def get(self, user_id):
        my_db = MyDBConnection("db/gotCrawler.db")
        user = UserController.get_one_from_id(int(user_id), my_db)
        return user.to_json()
