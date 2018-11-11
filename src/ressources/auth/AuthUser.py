from datetime import datetime
import jwt

from flask_restful import Resource
from flask import request

from src.controllers.UserController import UserController
from src.db.MyDBConnection import MyDBConnection
from src.config import CONFIG

class Authuser(Resource):
    """
        Signup a user
    """
    def post(self):
        my_db = MyDBConnection("db/gotCrawler.db")
        posted_data = request.get_json()
        user = UserController.get_one_from_cred(
            posted_data["params"]["login"],
            posted_data["params"]["pwd"],
            my_db
        )
        if user is not None:
            # we use the entire user to create the jwt
            encoded_jwt = jwt.encode(
                {
                    "user": {
                        "id": user.id,
                        "firstname": user.firstname,
                        "surname": user.surname,
                        "poster": user.poster
                    },
                    "exp": datetime.utcnow().timestamp() + 3600 * 24 * 3 #3 days
                },
                CONFIG['jwt_secret_key'],
                algorithm='HS256'
            )
            # by default the jwt is binary so we convert it to ascii
            return encoded_jwt.decode('ascii')
        else:
            return "Wrong credentials", 401