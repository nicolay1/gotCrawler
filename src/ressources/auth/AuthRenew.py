from datetime import datetime
import jwt

from flask_restful import Resource
from flask import request

from src.config import CONFIG

class AuthRenew(Resource):
    """
        Signup a user
    """
    def get(self):
        authorization_header = request.headers.get('Authorization')

        if not authorization_header:
            return "Error, no bearer token provided", 401
            
        # authorization_header = 'Bearer MyJwt.indifu213snas5difusnif'
        jwt_token = authorization_header[7:]
        try:
            jwt_decoded_token = jwt.decode(jwt_token, CONFIG['jwt_secret_key'])
        except jwt.exceptions.DecodeError:
            return "Error, this token is not correct", 401
        
        encoded_jwt = jwt.encode(
            {
                "user": jwt_decoded_token["user"],
                "exp": datetime.utcnow().timestamp() + 3600 * 24 * 3 #3 days
            },
            CONFIG['jwt_secret_key'],
            algorithm='HS256'
        )
        # by default the jwt is binary so we convert it to ascii
        return encoded_jwt.decode('ascii')