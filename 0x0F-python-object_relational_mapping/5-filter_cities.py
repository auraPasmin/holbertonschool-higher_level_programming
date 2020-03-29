#!/usr/bin/python3
"""
Write a script that takes in the name of a state as
ian argument and lists all cities o that state, using the database
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    """Connect to database."""
    ct_db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3])

    """Create cursor to exec queries using SQL."""
    cursor = ct_db.cursor()
    search_name = "SELECT cities.name\
                FROM cities\
                LEFT JOIN states\
                ON cities.state_id = states.id\
                ORDER BY cities.id ASC"

    cursor.execute(search_name, (name_inp,))
    separator = ""
    for row in cursor.fetchall():
        print("{}{}".format(separator, row[0]), end="")
        separator = ", "
    print("")
    cursor.close()
    ct_db.close()
