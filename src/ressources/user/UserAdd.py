from flask_restful import Resource
from flask import request

from src.controllers.UserController import UserController
from src.db.MyDBConnection import MyDBConnection

from src.helper.auth_decorators import authentication_required

from src.ressources.auth import AuthUser

from src.errors import ErrorUserAlreadyExist

class UserAdd(Resource):
    """
        Signup a user
    """

    method_decorators = [authentication_required]

    def post(self):
        my_db = MyDBConnection("db/gotCrawler.db")
        posted_data = request.get_json()
        try:
            new_user = UserController.add_user(
                posted_data["params"]["firstname"],
                posted_data["params"]["surname"],
                posted_data["params"]["login"],
                posted_data["params"]["pwd"],
                posted_data["params"]["poster"],
                my_db)
        except ErrorUserAlreadyExist:
            return ErrorUserAlreadyExist.flask_desc_code()
        return AuthUser.create_user_token(new_user).decode('ascii')
