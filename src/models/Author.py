from src.models.Person import Person


class Author(Person):
    """
    This class inherits of the Person class.
    """
    def __init__(self, name: str, surname: str):
        Person.__init__(self, name, surname)