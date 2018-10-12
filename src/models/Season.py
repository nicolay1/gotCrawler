from typing import List
from src.models.Episode import *


class Season:

    """
        This class represents a season of a show, populated from api
    """

    def __init__(self, id_show: int, num_season: int, list_episodes: List[Episode]):
        self.id_show = id_show
        self.num_season = num_season
        self.list_episodes = list_episodes

    @property
    def id_show(self):
        return self.__id_show

    @id_show.setter
    def id_show(self, id_show : int):
        if type(id_show) is not int:
            raise TypeError("Show id must be an integer")
        else:
            self.__id_show = id_sow

    @property
    def num_season(self):
        return self.__num_season

    @num_season.setter
    def num_season(self, num_season : int):
        if type(num_season) is not int:
            raise TypeError("Season number must be an integer")
        else:
            self.__num_season = num_season

    @property
    def list_episodes(self):
        return self.__list_episodes

    @list_episodes.setter
    def list_episodes(self, list_episodes : List[Episode]):
        if type(list_episodes) is not List[Episode]:
            raise TypeError("Episodes list must be a list of episodes")
        else:
            self.__list_episodes = list_episodes
