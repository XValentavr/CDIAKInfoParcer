import mysql
from mysql.connector import MySQLConnection, Error


def connect():
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='genealogyboutique',
                                       user='root',
                                       password='root')

    except Error as e:
        print('Error:', e)

    finally:
        return conn
