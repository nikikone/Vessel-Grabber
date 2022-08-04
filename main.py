import pymysql
from config import host, user, password, db_name
from pymysql.cursors import DictCursor
from Input_db import Input_db
from Output_db import Output_db
#try:
#    connect = pymysql.connect(
#        host=host,
#        port=3306,
#        user=user,
#        password=password,
#        database=db_name,
#        cursorclass=pymysql.cursors.DictCursor
#    )
#    print("Successfully connected...")
#    print('#' * 20)
#
#    try:
#        with connect.cursor() as cursor:
#            create_table_query = "CREATE TABLE Vessels (num int AUTO_INCREMENT, "\
#                                "id int, " \
#                                "latitude float, " \
#                                "longitude float, " \
#                                "speed int, " \
#                                "course int, " \
#                                "heading int, " \
#                                "destination varchar(22), " \
#                                "flag varchar(3), " \
#                                "length int, " \
#                                "width int, " \
#                                "rotation int, " \
#                                "name varchar(32), " \
#                                "type varchar(22), " \
#                                "deadweight int, " \
#                                "PRIMARY KEY(num));"
#
#            show = "SELECT * FROM Vessels;"
#            print(cursor.execute(show))
#            print("Table created successfully")
#    finally:
#        connect.close()
#except Exception as ex:
#    print("Connection refused...")
#    print(ex)


#def print_hi(name):
#    # Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    widget = QtWidgets.QDialog()
    dialog = Ui_MainWindow()
    Ui_MainWindow.setupUi(widget)
    #print_hi('PyCharm')
    #input_db = Input_db()
    #vessel = [2, 1.1, 1.1, 20, 25, 43, 'destination31', 'RUS', 14, 8, 4, 'Bolsoy', 'shipper', 26]
    #input_db.input_for_base(vessel)
    #output_db = Output_db()
    #output_db.output_visualizer("")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
