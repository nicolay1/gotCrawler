from typing import List
from src.models.Actor import *
from src.models.Author import *


class Episode:
    """
        This class represents an episode from a show, populated from the api
    """

    def __init__(self, name: str, id_season: int, num_ep: int, summary: str, list_actor: List[Actor],
                 list_author: List[Author]):

        self.__set_name(name)
        self.__set_id_season(id_season)
        self.__set_num_ep(num_ep)
        self.__set_summary(summary)
        self.__set_list_actor(list_actor)
        self.__set_list_author(list_author)

    @property
    def name(self):
        return self.__name

    def __set_name(self, name: str):
        if type(name) is not str:
            raise TypeError("Name should be a string")
        else:
            self.__name = name

    @property
    def id_season(self):
        return self.__id_season

    def __set_id_season(self, id_season: int):
        if type(id_season) is not int:
            raise TypeError("Season Id must be an integer")
        else:
            self.__id_season = id_season

    @property
    def num_ep(self):
        return self.__num_ep

    def __set_num_ep(self, num_ep: int):
        if type(num_ep) is not int:
            raise TypeError("Episode number must be an integer")
        else:
            self.__num_ep = num_ep

    @property
    def summary(self):
        return self.__summary

    def __set_summary(self, summary):
        if type(summary) is not str:
            raise TypeError("Summary should be a string")
        else:
            self.__summary = summary

    @property
    def list_actor(self):
        return self.__list_actor

    def __set_list_actor(self, list_actor: List[Actor]):
        if type(list_actor) is not List[Actor]:
            raise TypeError("Actor's list should be a list")
        else:
            self.__list_actor = list_actor

    @property
    def list_author(self):
        return self.__list_author

    def __set_list_author(self, list_author: List[Author]):
        if type(list_author) is not List[Author]:
            raise TypeError("Author's list should be a list")
        else:
            self.__list_author = list_author
