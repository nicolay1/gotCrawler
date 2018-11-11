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
            posted_data["params"]["firstname"],
            posted_data["params"]["surname"],
            posted_data["params"]["login"],
            posted_data["params"]["pwd"],
            posted_data["params"]["poster"],
            my_db)
        return "ok"
