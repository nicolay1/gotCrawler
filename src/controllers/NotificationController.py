from src.models.Notification import *
from src.models.User import *
from src.models.Show import *

class NotificationController:


    """
    This controller manage the Notification model, create notifications when needed.
    """

    @classmethod
    def add_notification(cls, user:User, show:Show):
        pass

    @classmethod
    def update_notification(cls, notification: Notification, user :User, show : Show):
        pass

    @classmethod
    def delete_notification(cls, notification : Notification):
        notification.delete_notification_in_bdd()