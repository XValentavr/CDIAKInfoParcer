"""
This module creates local database connect
"""

# project imports
import mysql
# local imports
from mysql.connector import MySQLConnection, Error


def connect():
    """
    cteate local database connection
    :return: database connection
    """
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='genealogyboutique',
                                       user='root',
                                       password='root')

    except Error as e:
        print('Error:', e)

    finally:
        return conn
