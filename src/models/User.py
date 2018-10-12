from src.models.Serie import *
from typing import List


class User:

    def __init__(self, firstname: str, surname: str, login: str, pwd: str, poster: str,
                 list_preferences: List[Serie]=None, id:int = None):
        self.__id = id
        self.__firstname = firstname
        self.__surname = surname
        self.__login = login
        self.__pwd = pwd
        self.__poster = poster
        self.__list_preferences = list_preferences

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self,value):
        if value == None :
            self.__id=0
        elif type(value) is not int:
            raise TypeError("Id should be an integer")
        else :
            self.__id = value



    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, value):
        if type(value) is not str:
            raise TypeError("Firstname should be a string")
        else:
            self.__firstname = value

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        if type(value) is not str:
            raise TypeError("Surname should be a string")
        else:
            self.__surname = value

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, value):
        if type(value) is not str:
            raise TypeError("Login should be a string")
        else:
            self.__login = value

    @property
    def pwd(self):
        return self.__pwd

    @pwd.setter
    def pwd(self, value):
        if type(value) is not str:
            raise TypeError("Password should be a string")
        else:
            self.__pwd = value

    @property
    def poster(self):
        return self.__poster

    @poster.setter
    def poster(self, value):
        if type(value) is not str:
            raise TypeError("Poster url should be a string")
        else:
            self.__poster = value

    @property
    def list_preferences(self):
        return self.__list_preferences

    @list_preferences.setter
    def list_preferences(self, value):
        if type(value) is not List[Serie]:
            raise TypeError("Poster url should be a string")
        else:
            self.__list_preferences = value


    def create_user_in_bdd(self):
        pass
        # TODO requete SQL
        # id = USERINBDD (id)

    def update_user_in_bdd(self, firstname: str = None, surname: str = None, login: str = None, pwd: str = None,
                           poster: str = None, list_preferences: List[Serie] = None):
        # TODO requete SQL
        self.__firstname = firstname
        self.__surname = surname
        self.__login = login
        self.__pwd = pwd
        self.__poster = poster
        self.__list_preferences = list_preferences

    def delete_user_in_bdd(self):
        #TODO requete SQL
        del self