from src.models.Person import Person


class Author(Person):
    """
    This class inherits of the Person class.
    """
    def __init__(self, name: str, role: str):
        Person.__init__(self, name)
        self.__set_role(role)

    @property
    def role(self):
        return self.__role

    def __set_role(self, role: str):
        if type(role) is not str and role is not None:
            raise TypeError("The attribute role of Author should be a string.")
        else:
            self.__role = role
