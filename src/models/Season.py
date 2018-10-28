from typing import List
from src.models.Episode import *


class Season:
    """
        This class represents a season of a show, populated from api
    """

    def __init__(self, id_show: int, num_season: int, name: str, poster: str,
                 overview: str, list_episodes: List[Episode]=None):
        self.__set_id_show(id_show)
        self.__set_num_season(num_season)
        self.__set_list_episodes(list_episodes)
        self.__set_name(name)
        self.__set_poster(poster)
        self.__set_overview(overview)

    @property
    def id_show(self):
        return self.__id_show

    def __set_id_show(self, id_show: int):
        if type(id_show) is not int:
            raise TypeError("Show id must be an integer")
        else:
            self.__id_show = id_sow

    @property
    def num_season(self):
        return self.__num_season

    def __set_num_season(self, num_season: int):
        if type(num_season) is not int:
            raise TypeError("Season number must be an integer")
        else:
            self.__num_season = num_season

    @property
    def list_episodes(self):
        return self.__list_episodes

    def __set_list_episodes(self, list_episodes: List[Episode]):
        if type(list_episodes) is not List[Episode] and list_episodes is not None:
            raise TypeError("Episodes list must be a list of episodes")
        else:
            self.__list_episodes = list_episodes

    @property
    def name(self):
        return self.__name

    def __set_name(self, name: str):
        if type(name) is not str:
            raise TypeError("Season name must be string")
        else:
            self.__name = name

    @property
    def poster(self):
        return self.__poster

    def __set_poster(self, poster: str):
        if type(poster) is not str:
            raise TypeError("Season poster must be string")
        else:
            self.__poster = poster

    @property
    def overview(self):
        return self.__overview

    def __set_overview(self, overview: str):
        if type(overview) is not str:
            raise TypeError("Season overview must be string")
        else:
            self.__overview = overview

    def to_json(self):
        return {
            "id_show": self.id_show,
            "num_season": self.num_season,
            "list_episodes": self.list_episodes,
            "name": self.name,
            "poster": self.poster,
            "overview": self.overview
        }
