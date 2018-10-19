from src.models.User import *
from src.models.Show import *
from src.models.Notification import *
from src.controllers.NotificationController import *
from src.controllers.ShowController import *
from src.db.MyDBConnection import MyDBConnection


class UserController:
    """
        This controller manages the User model
    """

    @classmethod
    def get_one(cls, login: str, pwd: str, my_db: MyDBConnection):
        return User.retrieve_user_from_credentials(login, pwd, my_db)

    @classmethod
    def add_user(cls, firstname: str, surname: str, login: str, pwd: str, poster: str, my_db: MyDBConnection,
                 list_preferences: List[Show] = None):
        user = User.retrieve_user_from_credentials(login, pwd, my_db)
        if user is None:
            user = User(firstname, surname, login, pwd, poster, list_preferences)
            user.create_user_in_bdd(my_db)

    @classmethod
    def update_user(cls, user: User, my_db: MyDBConnection, firstname: str = None, surname: str = None,
                    login: str = None, pwd: str = None,
                    poster: str = None,
                    list_preferences: List[Show] = None):
        user.update_user_in_bdd(my_db=my_db, firstname=firstname, surname=surname, login=login, pwd=pwd, poster=poster,
                                list_preferences=list_preferences)

    @classmethod
    def del_user(cls, user: User,my_db:MyDBConnection):
        user.delete_user_in_bdd(my_db=my_db)

    @classmethod
    def get_user_preference(cls, user: User):
        Notification.get_notification_from_user_id(user.id)

    @classmethod
    def add_preference_to_user(cls,user:User, api_id:int, my_db):
        show=ShowController.get_one_minimal_info(api_id,my_db)
        if show.id is None:
            ShowController.add_show(my_db,show.title,show.pict,show.api_id,show.season_next_episode_num, show.next_episode_num, show.date_next_episode)
        NotificationController.add_notification(user,show)

    @classmethod
    def delete_user_preference(cls,user:User,show:Show,my_db : MyDBConnection):
        notification=NotificationController.get_one(user,show, my_db)
        NotificationController.delete_notification(notification,my_db)
