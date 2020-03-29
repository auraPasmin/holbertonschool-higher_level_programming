#!/usr/bin/python3
"""
    Script that takes in an argument and displays all values
    in the states table of hbtn_0e_0_usa where name matches the argument.
"""

from sys import argv
import MySQLdb

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
    search_name = """
    SELECT * FROM states
    WHERE name LIKE BINARY '{:s}'
    ORDER BY id ASC""".format(argv[4])

    cursor.execute(search_name)
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    ct_db.close()
