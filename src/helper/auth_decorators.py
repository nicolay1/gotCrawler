
import functools
import flask
import jwt
import os

from src.config import CONFIG

def authentication_required(f):
    @functools.wraps(f)
    def decorated_function(*args, **kws):
        # we skip auth if we are in dev
        if os.environ['GC_ENV_TYPE'] == 'dev':
            return f(*args, **kws)
        
        authorization_header = flask.request.headers.get('Authorization')
        if not authorization_header:
            return "Error, no bearer token provided", 401
        
        # authorization_header = 'Bearer MyJwt.indifu213snas5difusnif'
        jwt_token = authorization_header[7:]
        try:
            decoded_jwt_token = jwt.decode(jwt_token, CONFIG['jwt_secret_key'])
        except jwt.exceptions.DecodeError:
            flask.abort(flask.Response(response="Error, this token is not correct", status=401))
        
        flask.request.user = decoded_jwt_token["user"]
        
        # everything is normal, we may move forward
        return f(*args, **kws)
        
    return decorated_function

def check_user_id(f):
    @functools.wraps(f)
    def decorated_function(*args, **kws):
        # we skip auth if we are in dev
        if os.environ['GC_ENV_TYPE'] == 'dev':
            return f(*args, **kws)
        
        # first, let's check that user_id is in kws, if it's not, it's a code
        # base error
        if "user_id" not in kws:
            raise ValueError("user_id was not present on func args \
associated with the check_user_id decorator.", flask.request)
        
        # same thing for the presence of user and the id key in the request
        # (which should have been populated by the jwt decorator)
        if not "user" in flask.request.__dict__ or "id" not in flask.request.user:
            raise ValueError("user should be into flask.request \
and should have an 'id' key", flask.request)

        # finaly we check that the id of the jwt owner is the same than the
        # user_id requested to retrieve a user ressource.
        print("Forbidden resource access: is {} but wanted {}".format(int(flask.request.user["id"]), int(kws["user_id"])))
        if int(flask.request.user["id"]) != int(kws["user_id"]):
            flask.abort(flask.Response(response="You do not have access to this ressource", status=401))

        # everything is normal, we may move forward
        return f(*args, **kws)
        
    return decorated_function