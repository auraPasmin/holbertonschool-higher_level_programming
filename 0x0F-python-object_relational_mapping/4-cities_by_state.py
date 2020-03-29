#!/usr/bin/python3
"""
Write a script that lists all cities from the database hbtn_0e_4_usa
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
    search_name = "SELECT cities.id, cities.name, states.name\
                FROM cities\
                LEFT JOIN states\
                ON cities.state_id = states.id\
                ORDER BY cities.id ASC"

    cursor.execute(search_name)
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    ct_db.close()
