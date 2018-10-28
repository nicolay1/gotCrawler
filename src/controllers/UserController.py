from typing import List

from src.models.User import User
from src.models.Show import Show
from src.models.Preference import Preference
from src.models.ShowPreference import ShowPreferences

from src.db.MyDBConnection import MyDBConnection

from .PreferenceController import PreferenceController
from .ShowController import ShowController

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
    def get_user_preference(user: User, my_db: MyDBConnection):
        return Preference.get_preference_from_user(user, my_db)
    
    @staticmethod
    def get_user_show_preferences(user: User, my_db: MyDBConnection):
        return ShowPreferences.get_show_preferences_from_user(user, my_db)

    @staticmethod
    def add_preference_to_user(user: User, api_id: int, my_db: MyDBConnection):
        show = ShowController.get_one_minimal_info(api_id, my_db)
        if show.id is None:
            ShowController.add_show(my_db, show.title, show.pict, show.api_id, show.season_next_episode_num,
                                    show.next_episode_num, show.date_next_episode)
        PreferenceController.add_preference(my_db, user, show, seen_flag=0)

    @staticmethod
    def delete_user_preference(user: User, show: Show, my_db: MyDBConnection):
        preference = PreferenceController.get_one(my_db, user, show)
        PreferenceController.delete_preference(my_db, preference)
