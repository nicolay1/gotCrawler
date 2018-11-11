# TODO vérifier l'import
from src.models.Season import Season
from typing import List
from datetime import datetime

from src.db.MyDBConnection import MyDBConnection

from src.helper import str_to_datetime, datetime_to_str


class Show:
    """
        The Show class represents a show.
        It is populated either from the database (for mandatory attributes for a show existing int the database), either
        from the API (for the rest).
        It contains necessarily a title (title), a picture (pict), the id used in the
        API (api_id), the next episode number and the corresponding season number (next_episode_num, set to None if it
        doesn't exist and season_next_episode_num), the date of next episode's diffusion (date_next_episode, None if
        next_episode == None) and the date of last update of date_next_episode (last_maj).
        db_id (id in the database), season_list (list of seasons), number_of_seasons and number_of_episodes are not
        mandatory.
    """

    def __init__(self,
                 title: str,
                 pict: str,
                 api_id: int,
                 season_next_episode_num: int = None,
                 next_episode_num: int = None,
                 date_next_episode: datetime = None,
                 last_maj: datetime = datetime.now().replace(microsecond=0),
                 db_id: int = None,
                 season_list: List[Season] = None,
                 number_of_episodes: int = None,
                 number_of_seasons: int = None,
                 overview: str = None):

        self.__set_title(title)
        self.__set_pict(pict)
        self.__set_api_id(api_id)
        self.__set_season_next_episode_num(season_next_episode_num)
        self.__set_next_episode_num(next_episode_num)
        self.__set_date_next_episode(date_next_episode)
        self.__set_last_maj(last_maj)
        self.__set_db_id(db_id)
        self.__set_season_list(season_list)
        self.__set_number_of_episodes(number_of_episodes)
        self.__set_number_of_seasons(number_of_seasons)
        self.__set_overview(overview)

    @property
    def title(self):
        return self.__title

    def __set_title(self, title: str):
        if type(title) is not str:
            raise TypeError("Title should be a string")
        else:
            self.__title = title

    @property
    def pict(self):
        return self.__pict

    def __set_pict(self, pict: str):
        if type(pict) is not str and pict is not None:
            raise TypeError("Pict url should be an string")
        else:
            self.__pict = pict

    @property
    def api_id(self):
        return self.__api_id

    def __set_api_id(self, api_id: int):
        if type(api_id) is not int:
            raise TypeError("api_id should be an integer")
        else:
            self.__api_id = api_id

    @property
    def season_next_episode_num(self):
        return self.__season_next_episode_num

    def __set_season_next_episode_num(self, season_next_episode_num: int):
        if type(season_next_episode_num) is not int and season_next_episode_num is not None:
            raise TypeError("season_next_episode_num should be an integer")
        else:
            self.__season_next_episode_num = season_next_episode_num

    @property
    def next_episode_num(self):
        return self.__next_episode_num

    def __set_next_episode_num(self, next_episode_num: int):
        if type(next_episode_num) is not int and next_episode_num is not None:
            raise TypeError("next_episode_num should be an integer")
        else:
            self.__next_episode_num = next_episode_num

    @property
    def date_next_episode(self):
        return self.__date_next_episode

    def __set_date_next_episode(self, date_next_episode: datetime):
        if type(date_next_episode) is not datetime and date_next_episode is not None:
            raise TypeError("date_next_episode should be a datetime")
        else:
            self.__date_next_episode = date_next_episode

    @property
    def last_maj(self):
        return self.__last_maj

    def __set_last_maj(self, last_maj: datetime):
        if type(last_maj) is not datetime:
            raise TypeError("The date of last update should be a datetime")
        else:
            self.__last_maj = last_maj

    @property
    def db_id(self):
        return self.__db_id

    def __set_db_id(self, db_id: int):
        if type(db_id) is not int and db_id is not None:
            raise TypeError("The DB Id should be an integer")
        else:
            self.__db_id = db_id

    @property
    def season_list(self):
        return self.__season_list

    def __set_season_list(self, season_list: List[Season]):
        # each object should be correctly populated
        self.__season_list = season_list

    @property
    def number_of_episodes(self):
        return self.__number_of_episodes

    def __set_number_of_episodes(self, number_of_episodes: int):
        if type(number_of_episodes) is not int and number_of_episodes is not None:
            raise TypeError("The number of episodes should be an integer")
        else:
            self.__number_of_episodes = number_of_episodes

    @property
    def number_of_seasons(self):
        return self.__number_of_seasons

    def __set_number_of_seasons(self, number_of_seasons: int):
        if type(number_of_seasons) is not int and number_of_seasons is not None:
            raise TypeError("The number of seasons should be an integer")
        else:
            self.__number_of_seasons = number_of_seasons

    @property
    def overview(self):
        return self.__overview

    def __set_overview(self, overview: str):
        if type(overview) is not str and overview is not None:
            raise TypeError("The overview should be a string")
        else:
            self.__overview = overview
    
    def associate_db_id(self, db_id: int):
        self.__set_db_id(db_id)

    def create_show_in_bdd(self, my_db: MyDBConnection):
        my_db.exec_one("""
        INSERT INTO show (pict, last_maj, title, season_next_episode_num, next_episode_date, next_episode_num, api_id) 
        VALUES ((?), (?), (?), (?), (?), (?), (?))""", (
            self.pict, self.last_maj, self.title, self.season_next_episode_num, self.date_next_episode,
            self.next_episode_num, self.api_id
        ))
        new_show = Show.retrieve_show_from_bdd(self.api_id, my_db)
        self.__set_db_id(new_show.db_id)

    def update_show(self, my_db: MyDBConnection, pict: str = None, season_next_episode_num: int = None,
                    next_episode_num: int = None, date_next_episode: datetime = None, season_list: List[Season] = None,
                    number_of_episodes: int = None, number_of_seasons: int = None):
        if pict is not None:
            self.__set_pict(pict)
        if season_next_episode_num is not None:
            self.__set_season_next_episode_num(season_next_episode_num)
        if next_episode_num is not None:
            self.__set_next_episode_num(next_episode_num)
        if date_next_episode is not None:
            self.__set_date_next_episode(date_next_episode)
            self.__set_last_maj(datetime.now().replace(microsecond=0))
        if season_list is not None:
            self.__set_season_list(season_list)
        if number_of_episodes is not None:
            self.__set_number_of_episodes(number_of_episodes)
        if number_of_seasons is not None:
            self.__set_number_of_seasons(number_of_seasons)
        my_db.exec_one("UPDATE SHOW SET pict=(?), last_maj=(?), season_next_episode_num=(?), next_episode_date=(?), "
                       "next_episode_num=(?) WHERE api_id=(?)",
                       (self.pict, datetime_to_str(self.last_maj), self.season_next_episode_num, datetime_to_str(self.date_next_episode),
                        self.next_episode_num,
                        self.api_id)
                       )

    @classmethod
    def retrieve_show_from_bdd(cls, api_id: int, my_db: MyDBConnection):
        show_res = my_db.exec_one("SELECT * from `show` WHERE api_id = (?)", (api_id))
        if not show_res:
            return None
        pict, last_maj, title, season_next_episode_num, next_episode_date, next_episode_num, api_id, db_id = show_res[0]
        
        return Show(title, pict, api_id, season_next_episode_num, next_episode_num, str_to_datetime(next_episode_date), str_to_datetime(last_maj), db_id)

    @staticmethod
    def get_all_with_a_pref(my_db: MyDBConnection):
        show_list = []
        list_shows_in_bdd = my_db.exec_one("""
            SELECT DISTINCT pict, last_maj, title, season_next_episode_num, next_episode_date, next_episode_num, api_id, show.id 
            FROM `show` JOIN preference
            WHERE preference.id_show = show.api_id""")
        if not list_shows_in_bdd:
            return None
        else:
            for show_res in list_shows_in_bdd:
                pict, last_maj, title, season_next_episode_num, next_episode_date, next_episode_num, api_id, db_id = show_res
                show_list.append(
                    Show(title, pict, api_id, season_next_episode_num, next_episode_num,
                         str_to_datetime(next_episode_date), str_to_datetime(last_maj), db_id)
                )
        return show_list

    def to_json(self):
        return {
            "title": self.title,
            "pict": "https://image.tmdb.org/t/p/w1280"+self.pict if self.pict is not None else None,
            "overview": self.overview,
            "api_id": self.api_id,
            "season_next_episode_num": self.season_next_episode_num,
            "next_episode_num": self.next_episode_num,
            "date_next_episode": datetime_to_str(self.date_next_episode) if self.last_maj is not None else None,
            "last_maj": datetime_to_str(self.last_maj) if self.last_maj is not None else None,
            "db_id": self.db_id,
            "season_list": [season.to_json() for season in self.season_list] if self.season_list else None,
            "number_of_episodes": self.number_of_episodes,
            "number_of_seasons": self.number_of_seasons
        }
