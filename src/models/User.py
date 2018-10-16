from typing import List

from models.Show import *
from db.MyDBConnection import MyDBConnection


class User:
    """
        This class represents our Users and is populated by the database
    """
    def __init__(self, firstname: str, surname: str, login: str, pwd: str, poster: str,
                 list_preferences: List[Show] = None, id:int = None):
        self.__setId(id)
        self.firstname = firstname
        self.surname = surname
        self.__setLogin(login)
        self.__setPwd(pwd)
        self.poster = poster
        self.list_preferences = list_preferences

    @property
    def id(self):
        return self.__id

    def __setId(self,id: int):
        if type(id) is not int and id is not None:
            raise TypeError("Id should be an integer")
        else :
            self.__id = id



    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname : str):
        if type(firstname) is not str:
            raise TypeError("Firstname should be a string")
        else:
            self.__firstname = firstname

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname : str):
        if type(surname) is not str:
            raise TypeError("Surname should be a string")
        else:
            self.__surname = surname

    @property
    def login(self):
        return self.__login

    def __setLogin(self, login : str):
        if type(login) is not str:
            raise TypeError("Login should be a string")
        else:
            self.__login = login

    @property
    def pwd(self):
        return self.__pwd

    def __setPwd(self, pwd : str):
        if type(pwd) is not str:
            raise TypeError("Password should be a string")
        else:
            self.__pwd = pwd

    @property
    def poster(self):
        return self.__poster

    @poster.setter
    def poster(self, poster : str):
        if type(poster) is not str:
            raise TypeError("Poster url should be a string")
        else:
            self.__poster = poster

    @property
    def list_preferences(self):
        return self.__list_preferences

    @list_preferences.setter
    def list_preferences(self, list_preferences : List[Show]):
        if type(list_preferences) is not List[Show] and list_preferences is not None:
            raise TypeError("List of preferences should be a list of preferences")
        else:
            self.__list_preferences = list_preferences


    def create_user_in_bdd(self, my_db: MyDBConnection):
        my_db.exec_one("""
        INSERT INTO user (surname, name, login, pwd, pict) VALUES 
        ((?), (?), (?), (?), (?))""", (
            self.firstname, self.surname, self.login, self.pwd, self.poster
        ))
        new_user = User.retrieve_user_from_credentials(self.login, self.pwd, my_db)
        self.__setId(new_user.id)

    def update_user_in_bdd(self, my_db: MyDBConnection, firstname: str = None, surname: str = None, login: str = None, pwd: str = None,
                           poster: str = None, list_preferences: List[Show]= None):
        if firstname is not None:
            self.firstname = firstname
        if surname is not None:
            self.surname = surname
        if login is not None:
            self.__setLogin(login)
        if pwd is not None:
            self.__setPwd(pwd)
        if poster is not None:
            self.poster = poster
        if list_preferences is not None:
            self.list_preferences = list_preferences
        my_db.exec_one("UPDATE USER SET firstname=(?), surname=(?), login=(?), pwd=(?), poster=(?) WHERE id=(?)", 
            (self.firstname, self.surname, self.login, self.pwd, self.poster, self.id)
        )
        # TODO apply update on preferences, maybe in the controller

    def delete_user_in_bdd(self, my_db: MyDBConnection):
        my_db.exec_one("DELETE from `user` WHERE `user`.id = (?)", (self.id))
        del self

    @classmethod
    def retrieve_user_from_credentials(cls, login: str, pwd: str, my_db: MyDBConnection):
        user_res = my_db.exec_one("SELECT * from `user` WHERE login = (?) AND pwd = (?)", (login, pwd))
        if not user_res:
            return None
        firstname, surname, login, pwd, poster, user_id = user_res[0]
        return User(firstname, surname, login, pwd, poster, id=user_id)
    
    def __str__(self):
        return """id:{}, firstname:{}, surname:{}, login:{}, poster:{}""".format(
            self.id, self.firstname, self.surname, self.login, self.poster
        )
