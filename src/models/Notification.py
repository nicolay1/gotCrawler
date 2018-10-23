from datetime import *

class Notification:

    """
    This class represents the notification that the user receive when the date of one of his favorite show next episode is getting close.
    """

    def __init__(self, id_user : int, id_show : int, num_season: int, num_ep : int, date_ep :datetime=None, id : int=None, seen_flag : bool=False):
                self.__set_id(id)
                self.__set_id_show(id_show)
                self.__set_id_user(id_user)
                self.__set_seen_flag(seen_flag)
                self.__set_num_ep(num_ep)
                self.__set_num_season(num_season)
                self.__set_date_ep(date_ep)

    @property
    def id(self):
        return self.__id

    def __set_id(self, id: int):
        if type(id) is not int and id is not None:
            raise TypeError("Id should be an integer")
        else :
            self.__id = id

    @property
    def id_show(self):
        return self.__id_show

    def __set_id_show(self, id_show: int):
        if type(id_show) is not int:
            raise TypeError("Show id should be an integer")
        else :
            self.__id_show = id_show

    @property
    def id_user(self):
        return self.__id_user

    def __set_id_user(self, id_user: int):
        if type(id_user) is not int:
            raise TypeError("User id should be an integer")
        else :
            self.__id_user = id_user
            
    @property
    def seen_flag(self):
        return  self.__seen_flag

    def __set_seen_flag(self, seen_flag : bool):
        if type(seen_flag) is not bool:
            raise TypeError("Seen flag should be a boolean")
        else:
            self.__seen_flag= seen_flag

    @property
    def num_ep(self):
        return self.__num_ep

    def __set_num_ep(self, num_ep : int):
        if type(num_ep) is not int:
            raise TypeError("Episode number should be an integer")
        else:
            self.__num_ep=num_ep

    @property
    def num_season(self):
        return self.__num_season

    def __set_num_season(self, num_season:int):
        if type(num_season) is not int:
            raise TypeError("Episode number should be an integer")
        else:
            self.__num_season=num_season

    @property
    def date_ep(self):
        return self.__date_ep

    def __set_date_ep(self, date_ep : datetime):
        if type(date_ep) is not datetime and date_ep is not None:
            raise TypeError("Date of episode should be a datetime")
        else:
            self.__date_ep=date_ep

    def set_as_seen(self):
        if self.seen_flag==False:
            self.__set_seen_flag(True)

    def set_as_not_seen(self):
        if self.seen_flag==True:
            self.__set_seen_flag(False)

    def create_notification_in_bdd(self):
        pass
    #TODO RQTE SQL

    def update_notification_in_bdd(self,num_season: int = None, num_ep : int = None, date_ep :datetime=None, seen_flag : bool=None ):
        if num_season is not None:
            self.__set_num_season(num_season)
        if num_ep is not None:
            self.__set_num_ep(num_ep)
        if date_ep is not None:
            self.__set_date_ep(date_ep)
        if seen_flag is not None:
            self.__set_seen_flag(seen_flag)
    #TODO RQT SQL

    def delete_notification_in_bdd(self):
        pass

    @classmethod
    def get_notification_from_user_id(cls,id_user : int):
        #return list of notification
        pass