# TODO vérifier l'import
from src.models.Season import Season
from typing import List
from datetime import datetime


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
                 season_next_episode_num: int,
                 next_episode_num: int,
                 date_next_episode: datetime,
                 last_maj: datetime,
                 db_id: int = None,
                 season_list: List[Season] = None,
                 number_of_episodes: int = None,
                 number_of_seasons: int = None):

        self.__setTitle(title)
        self.__setPict(pict)
        self.__setApi_id(api_id)
        self.__setSeason_next_episode_num(season_next_episode_num)
        self.__setNext_episode_num(next_episode_num)
        self.__setDate_next_episode(date_next_episode)
        self.__setLast_maj(last_maj)
        self.__setDb_id(db_id)
        self.__setSeason_list(season_list)
        self.__setNumber_of_episodes(number_of_episodes)
        self.__setNumber_of_seasons(number_of_seasons)
        
    @property
    def title(self):
        return self.__title

    def __setTitle(self, title: str):
        if type(title) is not str:
            raise TypeError("Title should be a string")
        else :
            self.__title = title
    
    @property
    def pict(self):
        return self.__pict

    def __setPict(self, pict: str):
        if type(pict) is not str:
            raise TypeError("Pict url should be an string")
        else :
            self.__pict = pict

    @property
    def api_id(self):
        return self.__api_id

    def __setApi_id(self, api_id: int):
        if type(api_id) is not int:
            raise TypeError("api_id should be an integer")
        else :
            self.__api_id = api_id

    @property
    def season_next_episode_num(self):
        return self.season_next_episode_num

    def __setSeason_next_episode_num(self, season_next_episode_num: int):
        if type(season_next_episode_num) is not int and season_next_episode_num is not None:
            raise TypeError("season_next_episode_num should be an integer")
        else :
            self.__season_next_episode_num = season_next_episode_num

    @property
    def next_episode_num(self):
        return self.__next_episode_num

    def __setNext_episode_num(self, next_episode_num: int):
        if type(next_episode_num) is not int and next_episode_num is not None:
            raise TypeError("next_episode_num should be an integer")
        else :
            self.__next_episode_num = next_episode_num

    @property
    def date_next_episode(self):
        return self.__date_next_episode

    def __setDate_next_episode(self, date_next_episode: datetime):
        if type(date_next_episode) is not datetime and date_next_episode is not None:
            raise TypeError("date_next_episode should be a datetime")
        else :
            self.__date_next_episode = date_next_episode

    @property
    def last_maj(self):
        return self.__last_maj

    def __setLast_maj(self, last_maj: datetime):
        if type(last_maj) is not datetime :
            raise TypeError("The date of last update should be a datetime")
        else :
            self.__last_maj = last_maj

    @property
    def db_id(self):
        return self.__db_id

    def __setDb_id(self, db_id: int):
        if type(db_id) is not int and db_id is not None:
            raise TypeError("The DB Id should be an integer")
        else:
            self.__db_id = db_id

    @property
    def season_list(self):
        return self.__season_list

    def __setSeason_list(self, season_list: List[Season]):
        if type(season_list) is not int and season_list is not None:
            raise TypeError("The season list should be list of seasons")
        else:
            self.__season_list = season_list

    @property
    def number_of_episodes(self):
        return self.__number_of_episodes

    def __setNumber_of_episodes(self, number_of_episodes: int):
        if type(number_of_episodes) is not int and number_of_episodes is not None:
            raise TypeError("The number of episodes should be an integer")
        else:
            self.__number_of_episodes = number_of_episodes

    @property
    def number_of_seasons(self):
        return self.__number_of_seasons

    def __setNumber_of_seasons(self, number_of_seasons: int):
        if type(number_of_seasons) is not int and number_of_seasons is not None:
            raise TypeError("The number of seasons should be an integer")
        else:
            self.__number_of_seasons = number_of_seasons


    