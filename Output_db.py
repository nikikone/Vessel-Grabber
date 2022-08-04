import pymysql
from config import host, user, password, db_name
from pymysql.cursors import DictCursor


class Output_db:

    @staticmethod
    def output_visualizer(where, number): # сделать просто отправку данных в метод update (точнее наоборот, вызов из update)

        try:
            connect = pymysql.connect(
                host=host,
                port=3306,
                user=user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor
            )
            print("Successfully connected to added...")
            print('-' * 20)

            try:
                with connect.cursor() as cursor:
                    #where2 = "WHERE id > 0 AND course = 25"
                    where2 = ""
                    #table_vessels = "SELECT * FROM mark " + where
                    if number == 1:
                        table_vessels = "SELECT t1.id, t1.latitude, t1.longitude, " \
                                        "t1.speed, t1.course, t1.heading, " \
                                        "t1.destination, t1.deadweight, t1.timedate," \
                                        " t2.flag, t2.name, t2.type FROM mark t1, " \
                                        "vessels t2 WHERE t1.id = t2.id " + where
                    elif number == 2:
                        table_vessels = "SELECT" \
                                        " id, flag, length, width, name, type, latitude, longitude FROM " \
                                        "vessels " + where
                    elif number == 3:
                        table_vessels = "SELECT id, latitude, longitude, " \
                                        "speed, course, heading, " \
                                        "type FROM satais " + where
                    elif number == 4:
                        table_vessels = "SELECT area_name, latitude_l_u, longitude_l_u, latitude_r_d, " \
                                        "longitude_r_d FROM parser"
                    # create_table_query = "CREATE TABLE Vessels (num int AUTO_INCREMENT, " \
                    #                     "id int, " \
                    #                     "latitude float, " \
                    #                     "longitude float, " \
                    #                     "speed int, " \
                    #                     "course int, " \
                    #                     "heading int, " \
                    #                     "destination varchar(22), " \
                    #                     "flag varchar(3), " \
                    #                     "length int, " \
                    #                     "width int, " \
                    #                     "rotation int, " \
                    #                     "name varchar(32), " \
                    #                     "type varchar(22), " \
                    #                     "deadweight int, " \
                    #                     "PRIMARY KEY(num));"
                    #selected = "SELECT * FROM vessels WHERE id = " + str(vessel[0]) + ";"
                    cursor.execute(table_vessels)
                    out = cursor.fetchall()
                    #print(out)
                    #for row in out:
                    #    print(row)
                    return out
            finally:
                connect.close()
        except Exception as ex:
            print("Connection refused...")
            print(ex)

    @staticmethod
    def output_export(): # создание файла с данными (пока не реализовано)
        try:
            connect = pymysql.connect(
                host=host,
                port=3306,
                user=user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor
            )
            print("Successfully connected to added...")
            print('-' * 20)

            try:
                with connect.cursor() as cursor:
                    #where2 = "WHERE id > 0 AND course = 25"
                    zapros_table = "SELECT * FROM Vessels " + where2
                    create_table_query = "CREATE TABLE Vessels (num int AUTO_INCREMENT, " \
                                         "id int, " \
                                         "latitude float, " \
                                         "longitude float, " \
                                         "speed int, " \
                                         "course int, " \
                                         "heading int, " \
                                         "destination varchar(22), " \
                                         "flag varchar(3), " \
                                         "length int, " \
                                         "width int, " \
                                         "rotation int, " \
                                         "name varchar(32), " \
                                         "type varchar(22), " \
                                         "deadweight int, " \
                                         "PRIMARY KEY(num));"
                    #selected = "SELECT * FROM vessels WHERE id = " + str(vessel[0]) + ";"
                    cursor.execute(zapros_table)
                    out = cursor.fetchall()
                    for row in out:
                        print(row)
                    return row
            finally:
                connect.close()
        except Exception as ex:
            print("Connection refused...")
            print(ex)