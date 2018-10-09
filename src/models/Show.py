# TODO vérifier l'import
from src.models.Season import Season
from typing import List
from datetime import datetime


class Show():
    """
        The Show class represents a show. It contains necessarily a title (title), a picture (pict), the id used in the
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
                 date_next_episode,
                 last_maj: datetime,
                 db_id: int = None,
                 season_list: List[Season] = None,
                 number_of_episodes: int = None,
                 number_of_seasons: int = None):

        self.__title = title
        self.__pict = pict
        self.__api_id = api_id
        self.__season_next_episode_num = season_next_episode_num
        self.__next_episode_num = next_episode_num
        self.__date_next_episode = date_next_episode
        self.__last_maj = last_maj
        self.__db_id = db_id
        self.__season_list = season_list
        self.__number_of_episodes = number_of_episodes
        self.__number_of_seasons = number_of_seasons
        
    @property
    def title(self):
        return self.__title
    
    @property
    def pict(self):
        return self.__pict

    @property
    def api_id(self):
        return self.__api_id

    @property
    def season_next_episode_num(self):
        return self.season_next_episode_num

    @property
    def next_episode_num(self):
        return self.__next_episode_num

    @property
    def date_next_episode(self):
        return self.__date_next_episode

    @property
    def last_maj(self):
        return self.__last_maj

    @property
    def db_id(self):
        return self.__db_id

    @property
    def season_list(self):
        return self.__season_list

    @property
    def number_of_episodes(self):
        return self.__number_of_episodes

    @property
    def number_of_seasons(self):
        return self.number_of_seasons

    @last_maj.setter
    def last_maj(self, new_datetime):
        if type(new_datetime) != datetime:
            raise TypeError("The last update of the date of next episode's diffusion has to be a datetime.")
        else:
            self.__last_maj = new_datetime
    