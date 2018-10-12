from src.models.Show import *
from typing import List


class User:

    """
        This class represents our User and is populated by the database
    """

    def __init__(self, firstname: str, surname: str, login: str, pwd: str, poster: str,
                 list_preferences: List[Show] =None, id:int = None):
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

    def __setId(self,id):
        if type(id) is not int and id is not None:
            raise TypeError("Id should be an integer")
        else :
            self.__id = id



    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname):
        if type(firstname) is not str:
            raise TypeError("Firstname should be a string")
        else:
            self.__firstname = firstname

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if type(surname) is not str:
            raise TypeError("Surname should be a string")
        else:
            self.__surname = surname

    @property
    def login(self):
        return self.__login

    def __setLogin(self, login):
        if type(login) is not str:
            raise TypeError("Login should be a string")
        else:
            self.__login = login

    @property
    def pwd(self):
        return self.__pwd

    def __setPwd(self, pwd):
        if type(pwd) is not str:
            raise TypeError("Password should be a string")
        else:
            self.__pwd = pwd

    @property
    def poster(self):
        return self.__poster

    @poster.setter
    def poster(self, poster):
        if type(poster) is not str:
            raise TypeError("Poster url should be a string")
        else:
            self.__poster = poster

    @property
    def list_preferences(self):
        return self.__list_preferences

    @list_preferences.setter
    def list_preferences(self, list_preferences):
        if type(list_preferences) is not List[Show] and list_preferences is not None:
            raise TypeError("List of preferences should be a list of preferences")
        else:
            self.__list_preferences = list_preferences


    def create_user_in_bdd(self):
        pass
        # TODO requete SQL
        # id = USERINBDD (id)

    def update_user_in_bdd(self, firstname: str = None, surname: str = None, login: str = None, pwd: str = None,
                           poster: str = None, list_preferences: List[Show]= None):
        # TODO requete SQL
        if firstname is not None :
            self.firstname = firstname
        if surname is not None:
            self.surname = surname
        if login is not None:
            self.__setLogin(login)
        if pwd is not None :
            self.__setPwd(pwd)
        if poster is not None :
            self.poster = poster
        if list_preferences is not None :
            self.list_preferences = list_preferences

    def delete_user_in_bdd(self):
        #TODO requete SQL
        del self

    @classmethod
    def retrieve_user_from_credentials(cls, login, pwd):
        pass
        #TODO SQL REQUEST
