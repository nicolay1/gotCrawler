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
        if not user:
            return None

        posted_data = request.get_json()
        show_id = posted_data["show_id"]

        # get the show from the id
        show = ShowController.get_on_from_db_w_api_id(my_db, show_id)
        if not show:
            return None

        PreferenceController.add_preference(my_db, user, show, 0)

        return "ok"
    
    def delete(self, user_id: int):
        my_db = MyDBConnection("db/gotCrawler.db")

        # retrieve the user from the id
        user = UserController.get_one_from_id(user_id, my_db)
        if not user:
            return None

        delete_data = request.get_json()
        show_id = delete_data["show_id"]

        # get the show from the id
        show = ShowController.get_on_from_db_w_api_id(my_db, show_id)
        if not show:
            return None

        try:
            PreferenceController.delete_preference(
                my_db, 
                PreferenceController.get_one_w_api_id(my_db, user, show)
            )
        except ValueError as err:
            return str(err), 500

        return "ok"
