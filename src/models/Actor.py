from src.models.Person import Person


class Actor(Person):
    """
        This class inherits of the Person class. Actor's objects have a picture (pict).
    """
    def __init__(self, name: str, pict: str):
        Person.__init__(self, name)
        self.__set_pict(pict)

    @property
    def pict(self):
        return self.__pict

    def __set_pict(self, pict: str):
        if type(pict) is not str:
            raise TypeError("The attribute pict of Actor should be a string.")
        else:
            self.__pict = pict
