from flask_restful import Resource

from src.controllers.ShowController import ShowController
from src.db.MyDBConnection import MyDBConnection

from src.errors import ErrorShowDoesNotExist

class ShowGet(Resource):
    """
        Get a show
    """
    def get(self, api_id):
        my_db = MyDBConnection("db/gotCrawler.db")
        api_id = int(api_id)
        try:
            show = ShowController.get_one_all_info(api_id, my_db)
        except ErrorShowDoesNotExist:
            return ErrorShowDoesNotExist.flask_desc_code()
        return show.to_json()
