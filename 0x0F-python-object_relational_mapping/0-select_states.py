#!/usr/bin/python3
# connect to mysql and list table state

import sys
import MySQLdb

if __name__ == '__main__':
    # arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # connect to database
    db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database,
            port=3306
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    records = cursor.fetchall()
    for row in records:
        print(row)
    cursor.close()
    db.close()
