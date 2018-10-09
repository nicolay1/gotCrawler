from typing import List
from src.models.Episode import *


class Season:

    def __init__(self, id_show: int, num_season: int, list_episodes: List[Episode]):
        self.__id_show = id_show
        self.__num_season = num_season
        self.__list_episodes = list_episodes

    @property
    def id_show(self):
        return self.__id_show

    @id_show.setter
    def id_show(self, value):
        if type(value) is not int:
            raise TypeError("Show id must be an integer")
        else:
            self.__id_show = value

    @property
    def num_season(self):
        return self.__num_season

    @num_season.setter
    def num_season(self, value):
        if type(value) is not int:
            raise TypeError("Season number must be an integer")
        else:
            self.__num_season = value

    @property
    def list_episodes(self):
        return self.__list_episodes

    @list_episodes.setter
    def list_episodes(self, value):
        if type(value) is not List[Episode]:
            raise TypeError("Episodes list must be a list of episodes")
        else:
            self.__list_episodes = value
