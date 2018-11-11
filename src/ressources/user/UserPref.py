from flask import request

from src.controllers.UserController import UserController
from src.controllers.PreferenceController import PreferenceController
from src.controllers.ShowController import ShowController

from src.db.MyDBConnection import MyDBConnection

from .User import UserRessource


class UserPref(UserRessource):
    """
        Get a user preferences
    """

    def get(self, user_id: int):
        my_db = MyDBConnection("db/gotCrawler.db")

        # retrieve the user from the id
        user = UserController.get_one_from_id(user_id, my_db)
        if not user:
            return None

        # retrieve preferences
        prefs = UserController.get_user_show_preferences(user, my_db)

        return [pref.to_json() for pref in prefs]

    def post(self, user_id: int):
        my_db = MyDBConnection("db/gotCrawler.db")

        # retrieve the user from the id
        user = UserController.get_one_from_id(user_id, my_db)
        if user is None:
            return "Error, this user does not exist"

        posted_data = request.get_json()
        show_id = posted_data["show_id"]

        # get the show from the id
        show = ShowController.get_or_create_from_db_w_api_id(my_db, show_id)
        if show is None:
            return "Error, the API does not know this Show.", 500

        PreferenceController.add_preference(my_db, user, show, 0)

        return "ok"
