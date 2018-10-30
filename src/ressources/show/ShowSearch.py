from flask_restful import Resource

from src.api_helper.ApiHelperTMDB import ApiHelperTMDB


class ShowSearch(Resource):
    """
        Search for a list of show
    """
    def search(self, query):
        show_list=[]
        for show in ApiHelperTMDB.get_search(query):
            show_list.append(show.to_json())
        return show_list


