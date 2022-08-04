import pymysql
from config import host, user, password, db_name
from pymysql.cursors import DictCursor


class Input_db:

    @staticmethod
    def check_for_new(vessel): # сделать просто отправку данных в метод update

        try:
            connect = pymysql.connect(
                host=host,
                port=3306,
                user=user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor
            )
            #print("Successfully connected to added...")
            #print('**' * 20)
            try:
                with connect.cursor() as cursor:
                    selected = "SELECT * FROM vessels WHERE id = " + str(vessel[0]) + ";"
                    print("Table selected successfully")

                    return cursor.execute(selected)
                    #print(cursor.execute(show))

                    #connect.commit()
            finally:
                connect.close()
        except Exception as ex:
            print("Connection refused...")
            print(ex)


    @staticmethod
    def input_for_base_area(area): #vessel too

        try:
            connect = pymysql.connect(
                host=host,
                port=3306,
                user=user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor
            )

            try:
                with connect.cursor() as cursor:
                    add_base_area = "INSERT INTO parser(area_name, latitude_l_u, " \
                               "longitude_l_u, latitude_r_d, longitude_r_d)" \
                               "VALUES (" \
                               + "'" + str(area['area_name']) + "'" + ", " \
                               + str(area['latitude_l_u']) + ", " \
                               + str(area['longitude_l_u']) + ", " \
                               + str(area['latitude_r_d']) + ", " \
                               + str(area['longitude_r_d']) + ");"
                    cursor.execute(add_base_area)
                    connect.commit()
            finally:
                connect.close()
        except Exception as ex:
            print("Connection refused...")
            print(ex)

    @staticmethod
    def input_for_base(vessels): #vessel too

        try:
            connect = pymysql.connect(
                host=host,
                port=3306,
                user=user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor
            )
            #print("Successfully connected to added...")
            #print('-' * 20)

            try:
                for k,v in vessels['mark'].items():
                    if vessels['mark'][k] is None:
                        vessels['mark'].update({k: "Null"})
                #print(vessels)
                #f = open("outTest.txt", "a")
                #f.write("Запустилась")
                #f.close()
                with connect.cursor() as cursor:
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
                    if vessels['ship'] is None:
                        selected = "SELECT * FROM satais WHERE id = " + "'" + str(vessels['mark']['id']) + "'" + ";"
                        if cursor.execute(selected) == 1: #проверка на наличие судна в БД, сделать добавление только метки. Реализовать добавление метки с временем её добавления
                            return
                            #print("Already added")
                        else:
                            # добавление пока что только судов, но сделать добавление и меток
                            add_base = "INSERT INTO satais(id, latitude, longitude, speed, course, " \
                                       "heading, type)" \
                                       "VALUES (" \
                                       + "'" + str(vessels['mark']['id']) + "'" + ", " \
                                       + str(vessels['mark']['latitude']) + ", " \
                                       + str(vessels['mark']['longitude']) + ", " \
                                       + str(vessels['mark']['speed']) + ", " \
                                       + str(vessels['mark']['course']) + ", " \
                                       + str(vessels['mark']['heading']) + ", " \
                                       + "'" + str(vessels['mark']['type']) + "'" \
                                       ");"
                            show = "SELECT * FROM vessels;"
                            #add_base_text = 'INSERT INTO SATAIS (id, latitude, longitude, speed, course, ' \
                            #                'heading, type) VALUES ("123", 12.2, 12.3, 14, 15, 16, "root");'
                            #add_base_num = (str(vessels['mark']['id']), float(vessels['mark']['latitude']), float(vessels['mark']['longitude']), int(vessels['mark']['speed']), int(vessels['mark']['course']),int(vessels['mark']['heading']), str(vessels['mark']['type']))
                            #add_base_num = (str("123"), float(12.2), float(12.3), int(14), int(15), int(16), str("rot"))
                            #print("1" * 20)
                            #print("SATAIS")
                            #print(add_base_num)
                            #add_base = "USE idata; INSERT INTO satais(id, latitude, longitude, speed, course, heading, type)VALUES ('TkRJeU16QTVOREl5TXpBNU5ESXlNdz09LTR4ZjBMcnRLK2tHTzN6b3Q4enI1VFE9PQ==', 42.99, 132.3033, 0, 13, Null, 'tag');"
                            #print(add_base) #1
                            cursor.execute(add_base)
                            #print(cursor.execute(show))
                            #print("Table added successfully")
                            connect.commit()
                    else:
                        selected_vessels = "SELECT * FROM vessels WHERE id = " + str(vessels['ship']['id']) + ";"

                        if cursor.execute(selected_vessels) == 1: #проверка на наличие судна в БД, сделать добавление только метки. Реализовать добавление метки с временем её добавления
                            selected_vessels_ll = "SELECT * FROM vessels WHERE id = " + str(vessels['ship']['id'])\
                                                  + " AND latitude = " + str(vessels['mark']['latitude']) + \
                                                  " AND longitude = " + \
                                                  str(vessels['mark']['longitude']) + ";"
                            if cursor.execute(selected_vessels_ll) == 1:
                                print("Already update ship")
                            else:
                                update_base_vessel = "REPLACE INTO vessels(id, flag," \
                                                     " length, width, name, type, latitude, longitude)" \
                                                     "VALUES (" \
                                                     + str(vessels['ship']['id']) + ", " \
                                                     + "'" + str(vessels['ship']['flag']) + "'" + ", " \
                                                     + str(vessels['ship']['length']) + ", " \
                                                     + str(vessels['ship']['width']) + ", " \
                                                     + "'" + str(vessels['ship']['name']) + "'" + ", " \
                                                     + "'" + str(vessels['ship']['type']) + "'" + ", " +\
                                                     str(vessels['mark']['latitude']) + ", " +\
                                                     str(vessels['mark']['longitude']) + \
                                                            ");"
                                #print(update_base_vessel)
                                cursor.execute(update_base_vessel)

                        else:
                            # добавление пока что только судов, но сделать добавление и меток
                            add_base_vessel = "INSERT INTO vessels(id, flag," \
                                       " length, width, name, type, latitude, longitude)" \
                                       "VALUES (" \
                                       + str(vessels['ship']['id']) + ", " \
                                       + "'" + str(vessels['ship']['flag']) + "'" + ", " \
                                       + str(vessels['ship']['length']) + ", " \
                                       + str(vessels['ship']['width']) + ", " \
                                       + "'" + str(vessels['ship']['name']) + "'" + ", " \
                                       + "'" + str(vessels['ship']['type']) + "'" + ", " +\
                                       str(vessels['mark']['latitude']) + ", " +\
                                       str(vessels['mark']['longitude']) + \
                                              ");"
                            show = "SELECT * FROM vessels;"
                            #print("2"*20)
                            #print("Vessel")
                            #print(add_base_vessel)
                            #2
                            cursor.execute(add_base_vessel)
                            #print(cursor.execute(show))
                            #print("Table added successfully")
                            #connect.commit()

                        selected_mark = "SELECT * FROM mark WHERE id = " + \
                                        str(vessels['ship']['id']) + " AND latitude = " + \
                                        str(vessels['mark']['latitude']) + \
                                        " AND longitude = " + \
                                        str(vessels['mark']['longitude']) + ";"
                        #selected_mark = "SELECT * FROM mark WHERE id = " + \
                        #                str(vessels['ship']['id']) + " AND CAST(latitude AS DECIMAL) = CAST(" + \
                        #                str(vessels['mark']['latitude']) + \
                        #                " AS DECIMAL) AND CAST(longitude AS DECIMAL) = CAST(" + \
                        #                str(vessels['mark']['longitude']) + " AS DECIMAL);"
                        if cursor.execute(
                                selected_mark) == 1:  # проверка на наличие судна в БД, сделать добавление только метки. Реализовать добавление метки с временем её добавления
                            print("Already added MARK")
                            connect.commit()
                        else:
                            # добавление пока что только судов, но сделать добавление и меток
                            add_base_mark = "INSERT mark(id, latitude, longitude, speed, course, " \
                                            "heading, destination, deadweight)" \
                                            "VALUES (" \
                                            + str(vessels['ship']['id']) + ", " \
                                            + str(vessels['mark']['latitude']) + ", " \
                                            + str(vessels['mark']['longitude']) + ", " \
                                            + str(vessels['mark']['speed']) + ", " \
                                            + str(vessels['mark']['course']) + ", " \
                                            + str(vessels['mark']['heading']) + ", " \
                                            + "'" + str(vessels['mark']['destination']) + "'" + ", " \
                                            + str(vessels['mark']['deadweight']) + \
                                            ");"
                            show = "SELECT * FROM vessels;"
                            # print("3"*20)
                            # print("Mark")
                            # print(add_base_mark)
                            # 3
                            cursor.execute(add_base_mark)
                            # print(cursor.execute(show))
                            # print("Table added successfully")
                            connect.commit()
            finally:
                connect.close()
        except Exception as ex:
            print("Connection refused...")
            print(ex)
