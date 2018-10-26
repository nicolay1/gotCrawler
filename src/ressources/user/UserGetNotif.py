from flask_restful import Resource

from src.controllers.UserController import UserController
from src.db.MyDBConnection import MyDBConnection

class UserGetNotif(Resource):
    """
        Get a user
    """
    def get(self, user_id):
        my_db = MyDBConnection("db/gotCrawler.db")
        user = UserController.get_one_from_id(user_id, my_db)
        notifs = UserController.get_user_notification(user, my_db)
        return [notif.to_json() for notif in notifs]
