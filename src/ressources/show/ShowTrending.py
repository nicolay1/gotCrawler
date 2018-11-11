from flask_restful import Resource
from flask import request

from src.api_helper.ApiHelperTMDB import ApiHelperTMDB


class ShowTrending(Resource):
    """
        Return list of trending show
    """
    def get(self):
        show_list=[]
        for show in ApiHelperTMDB().get_trending():
            show_list.append(show.to_json())
        return show_list


