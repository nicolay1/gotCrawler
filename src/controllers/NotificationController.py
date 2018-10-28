from src.models.Notification import *
from src.models.User import *
from src.models.Show import *
from src.db.MyDBConnection import MyDBConnection


class NotificationController:
    """
        This controller manage the Notification model, create notifications when needed.
    """
    @staticmethod
    def get_one(my_db: MyDBConnection, user: User, show: Show):
        notification = Notification.retrieve_notification_from_bdd(my_db=my_db, id_user=user.id, id_show=show.db_id)
        return notification

    @staticmethod
    def add_notification(my_db: MyDBConnection, user: User, show: Show, seen_flag: bool):
        notification = Notification.retrieve_notification_from_bdd(my_db=my_db, id_user=user.id, id_show=show.db_id)
        if notification is None:
            notification = Notification(id_user=user.id, id_show=show.db_id, seen_flag=seen_flag)
            notification.create_notification_in_bdd(my_db)

    @classmethod
    def update_notification(cls, my_db: MyDBConnection, notification: Notification, show: Show, seen_flag):
        notification.update_notification_in_bdd(my_db=my_db, seen_flag=seen_flag)

    @staticmethod
    def delete_notification(my_db: MyDBConnection, notification: Notification):
        notification.delete_notification_in_bdd(my_db=my_db)
