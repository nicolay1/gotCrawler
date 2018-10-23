import requests

from typing import Dict, Tuple
from urllib.parse import urljoin


class ApiHelper:
    """
        This class provide a class reference which may be used to call any API.
    """
    def __init__(self, root_api: str, default_query_params: Dict):
        self.__set_root_api(root_api)
        self.__set_default_query_params(default_query_params)
    
    @staticmethod
    def __build_query_params_uri(query_params: Dict):
        return '?' + '&'.join(
                [
                     "{}={}".format(
                        key,
                        query_params[key]
                    ) for key in query_params.keys()
                ]
            )

    def _get(self, ressource_path: str, path_param: Tuple = None, query_params: Dict = None):
        # First we define query params (which are the ones after the '?')
        if query_params is None:
            query_params = self.default_query_params
        else:
            query_params = dict(self.default_query_params, **query_params)
        query_params_str = ApiHelper.__build_query_params_uri(query_params)

        # the we build the complete path
        if path_param is None:
            url = urljoin(self.root_api, ressource_path) + query_params_str
        else:
            url = urljoin(self.root_api, ressource_path.format(*path_param)) + query_params_str
        
        print("Built url : {}".format(url))
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return None

    @property
    def root_api(self):
        return self.__root_api

    def __set_root_api(self, root_api: str):
        if type(root_api) is not str:
            raise TypeError("Root API should be a string")
        else:
            self.__root_api = root_api

    @property
    def default_query_params(self):
        return self.__default_query_params

    def __set_default_query_params(self, default_query_params: Dict):
        if type(default_query_params) is not dict:
            raise TypeError("Default query params API should be a dict")
        else:
            self.__default_query_params = default_query_params
