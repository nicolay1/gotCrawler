from abc import ABC


class Person(ABC):
    """
        Abstract class of which Actor and Author inherit.
    """
    def __init__(self, name: str, surname: str):
        self.__name = name
        self.__surname = surname

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if type(name) != str:
            raise TypeError("The attribute name of Person should be a string.")
        else:
            self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if type(surname) != str:
            raise TypeError("The attribute surname of Person should be a string.")
        else:
            self.__surname = surname
