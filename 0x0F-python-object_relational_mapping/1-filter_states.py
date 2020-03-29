#!/usr/bin/python3
"""
    Script that lists states with a name starting with N (upper N)
    from the database hbtn_0e_0_usa.
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
    cursor.execute("""SELECT * FROM states
                    WHERE name LIKE BINARY 'N%' ORDER BY id ASC""")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    ct_db.close()
