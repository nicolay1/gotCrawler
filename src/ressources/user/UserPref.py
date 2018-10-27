from flask_restful import Resource

from src.controllers.UserController import UserController
from src.controllers.PreferenceController import PreferenceController
from src.db.MyDBConnection import MyDBConnection

class UserGetPref(Resource):
    """
        Get a user
    """
    def get(self, user_id):
        my_db = MyDBConnection("db/gotCrawler.db")

        # retrieve the user from the id
        user = UserController.get_one_from_id(user_id, my_db)
        if not user:
            return None

        # retrieve preferences
        prefs = UserController.get_user_show_preferences(user, my_db)
        if not prefs:
            return None

        return [pref.to_json() for pref in prefs]
    
    # def post(self, user_id):
    #     my_db = MyDBConnection("db/gotCrawler.db")

    #     # retrieve the user from the id
    #     user = UserController.get_one_from_id(user_id, my_db)
    #     if not user:
    #         return None
        
    #     posted_data = request.get_json()
    #     show_id = posted_data["show_id"]

    #     # retrieve preferences
    #     prefs = PreferenceController.add_preference(my_db, user, )
    #     if not prefs:
    #         return None

    #     return [pref.to_json() for pref in prefs]
