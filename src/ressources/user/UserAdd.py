from flask_restful import Resource
from flask import request

from src.controllers.UserController import UserController
from src.db.MyDBConnection import MyDBConnection

from src.helper.auth_decorators import authentication_required

class UserAdd(Resource):
    """
        Signup a user
    """

    method_decorators = [authentication_required]

    def post(self):
        my_db = MyDBConnection("db/gotCrawler.db")
        posted_data = request.get_json()
        UserController.add_user(
            posted_data["firstname"],
            posted_data["surname"],
            posted_data["login"],
            posted_data["pwd"],
            posted_data["poster"],
            my_db)
        return "ok"
