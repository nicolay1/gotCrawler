from flask_restful import Resource

from src.controllers.ShowController import ShowController
from src.db.MyDBConnection import MyDBConnection


class ShowGet(Resource):
    """
        Get a show
    """
    def get(self, api_id):
        my_db = MyDBConnection("db/gotCrawler.db")
        show = ShowController.get_one_all_info(api_id, my_db)
        return show.to_json()
