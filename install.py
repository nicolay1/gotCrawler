from src.db.MyDBConnection import MyDBConnection
import os

DB_FILENAME = 'db/gotCrawler.db'

if os.path.isfile(DB_FILENAME) and input("Woops, a database already exist, remove it ? (y/n) : ") == 'y':
    os.remove(DB_FILENAME)

with open('db/create_and_seed.sql') as sql_file:
    my_db_connection = MyDBConnection(DB_FILENAME)
    queries = sql_file.read().split(';')
    my_db_connection.exec_mul(queries)
