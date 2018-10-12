from src.db.MyDBConnection import MyDBConnection

with open('db/create_and_seed.sql') as sql_file:
    my_db_connection = MyDBConnection('db/gotCrawler.db')
    queries = sql_file.read().split(';')
    my_db_connection.exec_mul(queries)
    print([i for i in my_db_connection.exec_one('SELECT * from user')])