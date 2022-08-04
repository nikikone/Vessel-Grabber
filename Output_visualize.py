import pymysql
from config import host, user, password, db_name
from pymysql.cursors import DictCursor
from Output_db import Output_db

class Output_visualize(object):

    def visualize_all(self, where): # чтобы сделать преобразование под нужный формат, нужно сначала разобраться, какой формат нужный)))

        visualize_db = Output_db()
        result = visualize_db.output_visualizer(where)
        return result

    def update(self): # тоже самое, что и выше

        visualize_db = Output_db()
        result = visualize_db.output_visualizer(where)
        return result