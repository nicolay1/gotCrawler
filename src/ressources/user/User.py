from flask_restful import Resource

from src.helper import authentication_required, check_user_id

class UserRessource(Resource):
    """
        User resources need to get the correct user_id and the correct authentication
    """
    method_decorators = [check_user_id, authentication_required]