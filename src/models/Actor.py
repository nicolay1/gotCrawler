from src.models.Person import Person


class Actor(Person):
    """
        This class inherits of the Person class. Actor's objects have a picture (pict).
    """
    def __init__(self, name: str, surname: str, pict: str):
        Person.__init__(self, name, surname)
        self.__pict = pict

    @property
    def pict(self):
        return self.__pict

    @pict.setter
    def pict(self, pict: str):
        if type(pict) is not str:
            raise TypeError("The attribute pict of Actor should be a string.")
        else:
            self.__pict = pict
