import sqlite3
from typing import List, Dict, Tuple


class MyDBConnection:
    """
        This class is aimed to handle every database calls, it use SQLite3
        in order to perform this. We may use one connection by Thread
    """

    def __init__(self, path_to_db):
        self.__db_connexion = sqlite3.connect(
            path_to_db, check_same_thread=False)

    def exec_mul(self, queries: List[str]) -> List[Dict[str, Tuple]]:
        """
            queries: the query list to be executed
            result: a list of dict which "result" key yield every rows from the 
            SQL result
            [{
                "query": query,
                "result": sql_result
            },...]
        """

        # this function is the same than exec_one but handle multiple queries
        # we made a copy past because the cursor must be create OUTSIDE the loop

        # we need to create a cursor to execute query(ies) and commit them (
        # to be sure they have been executed)
        cursor = self.__db_connexion.cursor()

        query_results = []

        for query in queries:
            # just checking that the query is a string
            if type(query) is not str:
                raise TypeError("query param is not a str")
            # we execute the query and fetch the result, for now, we do not
            # catch error waiting for an error handler.
            query_results.append({
                "query": query,
                "result": cursor.execute(query)
            })

        # once all the queries have been executed, we commit the result
        self.__db_connexion.commit()

        # we finaly return the result
        return query_results

    def exec_one(self, query: str, args: Tuple = (), selected_rows: Tuple = (), rows_as_objects: bool = False):
        """
            - query: the query to be executed
            - args: Tuple of args to be binded in the query
            - selected_rows: List of rows to be selected, used to force the 
                             output order.
                             ex : selected_rows = ['poster','user_id']
                             query = 'SELECT $rows FROM user'
                             => result : SELECT poster, user_id FROM user
            --
            result: an iterator which yield every rows from the SQL result
        """

        # just checking that the query is a string
        if type(query) is not str:
            raise TypeError("query param is not a str")

        # we need to create a cursor to execute query(ies) and commit them (to
        # be sure they have been executed)
        cursor = self.__db_connexion.cursor()

        # if selected rows is provided we concatenate them in the query
        if selected_rows:
            if not '$rows' in query:
                print("Warning, selected_rows provided but no $ detected")
            query = query.replace('$rows', ', '.join(selected_rows), 1)
        
        # if rows_as_objects is set as true, we use the __cast_rows_to_dicts
        # function, each row become a function.
        if rows_as_objects:
            cursor.row_factory = MyDBConnection.__cast_rows_to_dicts

        # we execute the query and fetch the result
        if type(args) is int or type(args) is float:
            args = [args]
        print("query '{}', is exectuded with ({}) args".format(query, args))

        # we retrieve the cursor ready to execute the query
        query_result_cursor = cursor.execute(query, args)

        # the commit make sure that all the precedent executed query have been
        # properly executed (especially in multi-threaded context)
        self.__db_connexion.commit()

        # we finally return the result
        return query_result_cursor.fetchall()

    @staticmethod
    def __cast_rows_to_dicts(cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    # @staticmethod
    # def __format_result(query_result: List, selected_rows: Tuple):
    #     if selected_rows:
    #         formated_result = {}
    #         for ind_row, row_data in enumerate(query_result):
    #             row_name = selected_rows[ind_row]
    #             formated_result[row_name] = row_data
    #     return query_result
