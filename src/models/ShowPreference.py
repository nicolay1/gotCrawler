from datetime import *
from flask import jsonify

from src.db.MyDBConnection import MyDBConnection

from .Preference import Preference
from .User import User
from .Show import Show

from datetime import date
from src.helper import datetime_to_str



class ShowPreferences:
    """
        Deal with preference which is a join of a Preference and a Show,
        actually just add the "seen_flag" to the Preference.
    """

    __db_rows = ['api_id', 'pict', 'next_episode_num', 'next_episode_date', 'season_next_episode_num', 'title', 'seen_flag']

    def __init__(self, api_id: int, pict: str, next_ep_num: int, next_ep_date: int,
                 next_season_num: date, title: str, new_ep_acknoweldged: int):
        self.__set_api_id(api_id)
        self.__set_pict(pict)
        self.__set_next_ep_num(next_ep_num)
        self.__set_next_ep_date(next_ep_date)
        self.__set_next_season_num(next_season_num)
        self.__set_title(title)
        self.__set_new_ep_acknoweldged(new_ep_acknoweldged)

    @property
    def api_id(self):
        return self.__api_id

    def __set_api_id(self, api_id: int):
        if type(api_id) is not int and api_id is not None:
            raise TypeError("api_id should be an int")
        else:
            self.__api_id = api_id

    @property
    def pict(self):
        return self.__pict

    def __set_pict(self, pict: str):
        if type(pict) is not str and pict is not None:
            raise TypeError("pict should be an string")
        else:
            self.__pict = pict

    @property
    def next_ep_num(self):
        return self.__next_ep_num

    def __set_next_ep_num(self, next_ep_num: int):
        if type(next_ep_num) is not int and next_ep_num is not None:
            raise TypeError("next_ep_num should be an integer")
        else:
            self.__next_ep_num = next_ep_num

    @property
    def next_ep_date(self):
        return self.__next_ep_date

    def __set_next_ep_date(self, next_ep_date: str):
        if type(next_ep_date) is not str and next_ep_date is not None:
            raise TypeError("next_ep_date should be an string")
        else:
            self.__next_ep_date = next_ep_date

    @property
    def next_season_num(self):
        return self.__next_season_num

    def __set_next_season_num(self, next_season_num: int):
        if type(next_season_num) is not int and next_season_num is not None:
            raise TypeError("next_season_num should be an integer")
        else:
            self.__next_season_num = next_season_num

    @property
    def title(self):
        return self.__title

    def __set_title(self, title: str):
        if type(title) is not str and title is not None:
            raise TypeError("title should be an string")
        else:
            self.__title = title

    @property
    def new_ep_acknoweldged(self):
        return self.__new_ep_acknoweldged

    def __set_new_ep_acknoweldged(self, new_ep_acknoweldged: int):
        if type(new_ep_acknoweldged) is not int and new_ep_acknoweldged is not None:
            raise TypeError("new_ep_acknoweldged should be an integer")
        else:
            self.__new_ep_acknoweldged = new_ep_acknoweldged

    @classmethod
    def get_show_preferences_from_user(cls, user: User, my_db: MyDBConnection):
        show_pref_db_res = my_db.exec_one("""
            SELECT $cols FROM show 
                JOIN preference ON preference.id_show = show.api_id
            WHERE preference.id_user = (?)""",
                       args=(user.id),
                       selected_rows=cls.__db_rows,
                       rows_as_objects=True
                       )
        
        show_preferences = []
        # we force the order in a way that the DB result has the perfect shape
        # for creating the object (with selected_rows).
        for row in show_pref_db_res:
            pop_args = [row[row_name] for row_name in ShowPreferences.__db_rows]
            show_preferences.append(cls(*pop_args))

        return show_preferences

    def to_json(self):
        return {
            "api_id": self.api_id,
            "pict": "https://image.tmdb.org/t/p/w1280"+self.pict if self.pict is not None else None,
            "next_ep_num": self.next_ep_num,
            #TODO quand la méthode get_show_preferences_from_user est corrigé !! "next_ep_date": datetime_to_str(self.next_ep_date),
            "next_ep_date": self.next_ep_date,
            "next_season_num": self.next_ep_num,
            "title": self.title,
            "new_ep_acknoweldged": self.new_ep_acknoweldged
        }
