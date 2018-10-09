from typing import List


class Episode:

    def __init__(self, name: str, id_season: int, num_ep: int, summary: str, list_actor: List[Actor],
                 list_author: List[Author]):

        self.__name = name
        self.__id_season = id_season
        self.__num_ep = num_ep
        self.__summary = summary
        self.__list_actor = list_actor
        self.__list_author = list_author

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if type(value) is not str:
            raise TypeError("Name should be a string")
        else:
            self.__name = value

    @property
    def id_season(self):
        return self.__id_season

    @id_season.setter
    def id_season(self, value):
        if type(value) is not int:
            raise TypeError("Season Id must be an integer")
        else:
            self.__id_season = value

    @property
    def num_ep(self):
        return self.__num_ep

    @num_ep.setter
    def num_ep(self, value):
        if type(value) is not int:
            raise TypeError("Episode number must be an integer")
        else:
            self.__num_ep = value

    @property
    def summary(self):
        return self.__summary

    @summary.setter
    def summary(self, value):
        if type(value) is not str:
            raise TypeError("Summary should be a string")
        else:
            self.__summary = value

    @property
    def list_actor(self):
        return self.__list_actor

    @list_actor.setter
    def list_actor(self, value):
        if type(value) is not List:  # TODO
            raise TypeError("Actor's list should be a list")
        else:
            self.__list_actor = value

    @property
    def list_author(self):
        return self.__list_author

    @list_author.setter
    def list_author(self, value):
        if type(value) is not List:  # TODO
            raise TypeError("Author's list should be a list")
        else:
            self.__list_author = value
