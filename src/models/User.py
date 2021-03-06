from typing import List

from src.models.Show import Show
from src.db.MyDBConnection import MyDBConnection


class User:
    """
        This class represents our Users and is populated by the database
    """

    def __init__(self, firstname: str, surname: str, login: str, pwd: str, poster: str,
                 list_preferences: List[Show] = None, new_id: int = None):
        self.__set_id(new_id)
        self.__set_firstname(firstname)
        self.__set_surname(surname)
        self.__set_login(login)
        self.__set_pwd(pwd)
        self.__set_poster(poster)
        self.__set_list_preferences(list_preferences)

    @property
    def id(self):
        return self.__id

    def __set_id(self, new_id: int):
        if type(new_id) is not int and new_id is not None:
            raise TypeError("Id should be an integer")
        else:
            self.__id = new_id

    @property
    def firstname(self):
        return self.__firstname

    def __set_firstname(self, firstname: str):
        if type(firstname) is not str:
            raise TypeError("Firstname should be a string")
        else:
            self.__firstname = firstname

    @property
    def surname(self):
        return self.__surname

    def __set_surname(self, surname: str):
        if type(surname) is not str:
            raise TypeError("Surname should be a string")
        else:
            self.__surname = surname

    @property
    def login(self):
        return self.__login

    def __set_login(self, login: str):
        if type(login) is not str:
            raise TypeError("Login should be a string")
        else:
            self.__login = login

    @property
    def pwd(self):
        return self.__pwd

    def __set_pwd(self, pwd: str):
        if type(pwd) is not str:
            raise TypeError("Password should be a string")
        else:
            self.__pwd = pwd

    @property
    def poster(self):
        return self.__poster

    def __set_poster(self, poster: str):
        if type(poster) is not str:
            raise TypeError("Poster url should be a string")
        else:
            self.__poster = poster

    @property
    def list_preferences(self):
        return self.__list_preferences

    def __set_list_preferences(self, list_preferences: List[Show]):
        if type(list_preferences) is not List[Show] and list_preferences is not None:
            raise TypeError(
                "List of preferences should be a list of preferences")
        else:
            self.__list_preferences = list_preferences

    def create_user_in_bdd(self, my_db: MyDBConnection):
        new_user = self.retrieve_user_from_credentials(
            self.login, self.pwd, my_db)
        if new_user is None:
            my_db.exec_one("""
            INSERT INTO user (surname, firstname, login, pwd, poster) VALUES 
            ((?), (?), (?), (?), (?))""", (
                self.firstname, self.surname, self.login, self.pwd, self.poster
            ))
            new_user = User.retrieve_user_from_credentials(
                self.login, self.pwd, my_db)
            self.__set_id(new_user.id)

    def update_user_in_bdd(self, my_db: MyDBConnection, firstname: str = None, surname: str = None, login: str = None, pwd: str = None,
                           poster: str = None, list_preferences: List[Show] = None):
        if firstname is not None:
            self.__set_firstname(firstname)
        if surname is not None:
            self.__set_surname(surname)
        if login is not None:
            self.__set_login(login)
        if pwd is not None:
            self.__set_pwd(pwd)
        if poster is not None:
            self.__set_poster(poster)
        if list_preferences is not None:
            self.__set_list_preferences(list_preferences)
        my_db.exec_one("UPDATE USER SET firstname=(?), surname=(?), login=(?), pwd=(?), poster=(?) WHERE id=(?)",
                       (self.firstname, self.surname, self.login,
                        self.pwd, self.poster, self.id)
                       )
        # TODO apply update on preferences, maybe in the controller

    def delete_user_in_bdd(self, my_db: MyDBConnection):
        my_db.exec_one("DELETE from `user` WHERE `user`.id = (?)", (self.id))
        del self

    @classmethod
    def retrieve_user_from_id(cls, user_id: int, my_db: MyDBConnection):
        user_res = my_db.exec_one("SELECT * from `user` WHERE id = (?)", (user_id))
        if not user_res:
            return None
        firstname, surname, login, pwd, poster, user_id = user_res[0]
        return User(firstname, surname, login, pwd, poster, new_id=user_id)

    @classmethod
    def retrieve_user_from_credentials(cls, login: str, pwd: str, my_db: MyDBConnection):
        user_res = my_db.exec_one(
            "SELECT * from `user` WHERE login = (?) AND pwd = (?)", (login, pwd))
        if not user_res:
            return None
        firstname, surname, login, pwd, poster, user_id = user_res[0]
        return User(firstname, surname, login, pwd, poster, new_id=user_id)

    def __str__(self):
        return """id:{}, firstname:{}, surname:{}, login:{}, poster:{}""".format(
            self.id, self.firstname, self.surname, self.login, self.poster
        )
    
    def to_json(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "surname": self.surname,
            "login": self.login,
            "poster": self.poster
        }
