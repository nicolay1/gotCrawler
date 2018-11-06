from flask_restful import Resource
from flask import request

from src.api_helper.ApiHelperTMDB import ApiHelperTMDB


class ShowSearch(Resource):
    """
        Search for a list of show
    """
    def get(self):
        show_list=[]
        query = request.args.get('q')
        for show in ApiHelperTMDB().get_search(query):
            show_list.append(show.to_json())
        return show_list


