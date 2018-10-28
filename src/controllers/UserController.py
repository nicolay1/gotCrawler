from src.models.User import *
from src.models.Show import *
from src.models.Notification import *

from src.db.MyDBConnection import MyDBConnection

from src.controllers.NotificationController import *
from src.controllers.ShowController import *


class UserController:
    """
        This controller manages the User model
    """
    def __init__(self):
        pass

    @staticmethod
    def get_one_from_cred(login: str, pwd: str, my_db: MyDBConnection):
        return User.retrieve_user_from_credentials(login, pwd, my_db)
    
    @staticmethod
    def get_one_from_id(user_id: int, my_db: MyDBConnection):
        return User.retrieve_user_from_id(user_id, my_db)

    @staticmethod
    def add_user(firstname: str, surname: str, login: str, pwd: str, poster: str, my_db: MyDBConnection,
                 list_preferences: List[Show] = None):
        user = User.retrieve_user_from_credentials(login, pwd, my_db)
        if user is None:
            user = User(firstname, surname, login, pwd, poster, list_preferences)
            user.create_user_in_bdd(my_db)

    @staticmethod
    def update_user(user: User, my_db: MyDBConnection, firstname: str = None, surname: str = None,
                    login: str = None, pwd: str = None,
                    poster: str = None,
                    list_preferences: List[Show] = None):
        user.update_user_in_bdd(my_db=my_db, firstname=firstname, surname=surname, login=login, pwd=pwd, poster=poster,
                                list_preferences=list_preferences)

    @staticmethod
    def del_user(user: User, my_db: MyDBConnection):
        user.delete_user_in_bdd(my_db=my_db)

    @staticmethod
    def get_user_notification(user: User, my_db: MyDBConnection):
        return Notification.get_notification_from_user(user, my_db)

    @staticmethod
    def add_preference_to_user(user: User, api_id: int, my_db: MyDBConnection):
        show = ShowController.get_one_minimal_info(api_id, my_db)
        if show.id is None:
            ShowController.add_show(my_db, show.title, show.pict, show.api_id, show.season_next_episode_num,
                                    show.next_episode_num, show.date_next_episode)
        NotificationController.add_notification(my_db, user, show, seen_flag=False)

    @staticmethod
    def delete_user_preference(user: User, show: Show, my_db: MyDBConnection):
        notification = NotificationController.get_one(my_db, user, show)
        NotificationController.delete_notification(my_db, notification)
