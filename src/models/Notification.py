from datetime import *
from src.db.MyDBConnection import MyDBConnection
from src.models.User import User
from src.models.Show import Show

class Notification:

    """
    This class represents the notification that the user receive when the date of one of his favorite show next episode
    is getting close.
    """

    def __init__(self, id_user: int, id_show: int, new_id: int=None, seen_flag: bool=False):
                self.__set_id(new_id)
                self.__set_id_show(id_show)
                self.__set_id_user(id_user)
                self.__set_seen_flag(seen_flag)

    @property
    def id(self):
        return self.__id

    def __set_id(self, new_id: int):
        if type(new_id) is not int and new_id is not None:
            raise TypeError("Id should be an integer")
        else:
            self.__id = new_id

    @property
    def id_show(self):
        return self.__id_show

    def __set_id_show(self, id_show: int):
        if type(id_show) is not int:
            raise TypeError("Show id should be an integer")
        else:
            self.__id_show = id_show

    @property
    def id_user(self):
        return self.__id_user

    def __set_id_user(self, id_user: int):
        if type(id_user) is not int:
            raise TypeError("User id should be an integer")
        else:
            self.__id_user = id_user
            
    @property
    def seen_flag(self):
        return self.__seen_flag

    def __set_seen_flag(self, seen_flag: bool):
        if type(seen_flag) is not bool:
            raise TypeError("Seen flag should be a boolean")
        else:
            self.__seen_flag = seen_flag

    def set_as_seen(self):
        if self.seen_flag == False:
            self.__set_seen_flag(True)

    def set_as_not_seen(self):
        if self.seen_flag == True:
            self.__set_seen_flag(False)

    def create_notification_in_bdd(self, my_db: MyDBConnection):
        my_db.exec_one("""
                INSERT INTO notification (id_user, id_show, seen_flag) VALUES 
                ((?), (?), (?))""", (
            self.id_user, self.id_show, self.seen_flag
        ))
        new_notif = Notification.retrieve_notification_from_bdd(my_db, self.id_user, self.id_show)
        self.__set_id(new_notif.id)

    @classmethod
    def retrieve_notification_from_bdd(cls, my_db: MyDBConnection, id_user: int, id_show: int):
        notification_res = my_db.exec_one("SELECT * from `notification` WHERE id_user = (?) AND id_show = (?)",
                                          (id_user, id_show))
        if not notification_res:
            return None
        id_user, id_show, seen_flag, new_id = notification_res[0]
        return Notification(id_user=id_user, id_show=id_show, seen_flag=seen_flag, new_id=new_id)

    def update_notification_in_bdd(self, my_db: MyDBConnection, seen_flag: bool):
        if seen_flag is not None:
            self.__set_seen_flag(seen_flag)
        my_db.exec_one("UPDATE NOTIFICATION SET id_user=(?), id_show=(?), seen_flag=(?), WHERE id=(?)",
                       (self.id_user, self.id_show, self.seen_flag, self.id)
                       )

    def delete_notification_in_bdd(self, my_db: MyDBConnection):
        my_db.exec_one("DELETE from `notification` WHERE `notification`.id = (?)", (self.id))
        del self

    @staticmethod
    def get_notification_from_user(user: User, my_db: MyDBConnection):
        if User is None:
            raise TypeError("The user from which we want to get notifications is not valid")
        else:
            list_notifications_res = my_db.exec_one("SELECT * from `notification` WHERE id_user = (?)", (user.id))
            list_notifications = []
            for notification in list_notifications_res:
                id_user, id_show, seen_flag, _ = notification
                list_notifications.append(Notification(id_user, id_show, seen_flag))
            return list_notifications


    @classmethod
    def get_notification_from_show(cls, show: Show, my_db: MyDBConnection):
        if show is None:
            raise TypeError("The show from which we want to get notifications is not valid")
        else:
            list_notifications = my_db.exec_one("SELECT * from `notification` WHERE id_show = (?)", (show.db_id))
            return list_notifications

    def to_json(self):
        return {
            "id": self.id,
            "id_show": self.id_show,
            "id_user": self.id_user,
            "seen_flag": self.seen_flag
        }
