from src.models.Notification import *
from src.models.User import *
from src.models.Show import *
from src.db.MyDBConnection import MyDBConnection


class NotificationController:
    """
        This controller manage the Notification model, create notifications when needed.
    """
    @classmethod
    def get_one(cls, my_db: MyDBConnection, user: User, show: Show):
        notification = Notification.retrieve_notification_from_bdd(id_user=user.id, id_show=show.db_id, my_db=my_db)
        return notification

    @classmethod
    def add_notification(cls, my_db: MyDBConnection, user: User, show: Show, seen_flag: bool):
        notification = Notification.retrieve_notification_from_bdd(id_user=user.id, id_show=show.db_id, my_db=my_db)
        if notification is None:
            notification = Notification(id_user=user.id, id_show=show.db_id, num_season=show.season_next_episode_num,
                                        num_ep=show.next_episode_num, date_ep=show.date_next_episode,
                                        seen_flag=seen_flag)
            notification.create_notification_in_bdd(my_db)

    @classmethod
    def update_notification(cls, my_db: MyDBConnection, notification: Notification, show: Show, seen_flag):
        notification.update_notification_in_bdd(my_db=my_db, num_season=show.season_next_episode_num,
                                                num_ep=show.next_episode_num, date_ep=show.date_next_episode,
                                                seen_flag=seen_flag)

    @classmethod
    def delete_notification(cls, my_db: MyDBConnection, notification: Notification):
        notification.delete_notification_in_bdd(my_db=my_db)
