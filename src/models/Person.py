from abc import ABC


class Person(ABC):
    """
        Abstract class of which Actor and Author inherit.
    """
    def __init__(self, name: str, surname: str):
        self.__set_name(name)
        self.__set_surname(surname)

    @property
    def name(self):
        return self._name

    def __set_name(self, name: str):
        if type(name) is not str:
            raise TypeError("The attribute name of Person should be a string.")
        else:
            self._name = name

    @property
    def surname(self):
        return self._surname

    def __set_surname(self, surname: str):
        if type(surname) is not str:
            raise TypeError("The attribute surname of Person should be a string.")
        else:
            self._surname = surname
