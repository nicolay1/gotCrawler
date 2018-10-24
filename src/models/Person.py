from abc import ABC


class Person(ABC):
    """
        Abstract class of which Actor and Author inherit.
    """
    def __init__(self, name: str):
        self.__set_name(name)

    @property
    def name(self):
        return self._name

    def __set_name(self, name: str):
        if type(name) is not str:
            raise TypeError("The attribute name of Person should be a string.")
        else:
            self._name = name
