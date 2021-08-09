#!/usr/bin/python3
"""
Module 0-select_states
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Data connection
    database = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = database.cursor()
    cursor.execute("SELECT * FROM `states` ORDER BY `states`.`id` ASC")
    All = cursor.fetchall()
    for row in All:
        print(row)
    # close db
    cursor.close()
    database.close()
