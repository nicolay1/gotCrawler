from flask import request

from src.controllers.UserController import UserController
from src.db.MyDBConnection import MyDBConnection
from src.errors import ErrorUserDoesNotExist

from .User import UserRessource

class UserGet(UserRessource):
    """
        Get a user
    """

    def get(self, user_id):
        my_db = MyDBConnection("db/gotCrawler.db")
        try:
            user = UserController.get_one_from_id(int(user_id), my_db)
        except ErrorUserDoesNotExist:
            return ErrorUserDoesNotExist.flask_desc_code()
        return user.to_json()
