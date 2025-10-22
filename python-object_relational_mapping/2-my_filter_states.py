#!/usr/bin/python3
"""
This script displays all values in an argument an display all value from
the states where name matches the argument.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """Access to the database and get the states from the database."""

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states \
                 WHERE name LIKE BINARY '{}' \
                 ORDER BY states.id ASC".format(argv[4]))
    rows = cur.fetchall()

    for row in rows:
        print(row)
