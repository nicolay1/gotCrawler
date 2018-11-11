from flask import request

from src.controllers.UserController import UserController
from src.controllers.PreferenceController import PreferenceController
from src.controllers.ShowController import ShowController
from src.config import CONFIG

from src.db.MyDBConnection import MyDBConnection

from .User import UserRessource

class UserPrefDelPut(UserRessource):
    """
        Get a user preferences
    """
    def delete(self, user_id: int, show_id: int):
        my_db = MyDBConnection(CONFIG["db_path"])

        user_id = int(user_id)
        show_id = int(show_id)

        # retrieve the user from the id
        user = UserController.get_one_from_id(user_id, my_db)
        if not user:
            return None

        # get the show from the id
        show = ShowController.get_or_create_from_db_w_api_id(my_db, show_id)
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

    def put(self, user_id: int, show_id: int):
        my_db = MyDBConnection(CONFIG["db_path"])

        user_id = int(user_id)
        show_id = int(show_id)

        # retrieve the user from the id
        user = UserController.get_one_from_id(user_id, my_db)
        if user is None:
            return "Error, this user does not exist"

        posted_data = request.get_json()
        new_seen_flag = posted_data["new_seen_flag"]

        show = ShowController.get_or_create_from_db_w_api_id(my_db, show_id);
        if show is None:
            return "Error, the API does not know this Show.", 500

        preference = PreferenceController.get_one_w_api_id(my_db, user, show)

        try:
            PreferenceController.update_preference_seen_flag(my_db, preference, new_seen_flag)
        except ValueError as err:
            return str(err), 500


        return "ok"
