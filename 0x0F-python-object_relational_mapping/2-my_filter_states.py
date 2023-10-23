#!/usr/bin/python3
""" script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches
the argument."""

import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY states.id ASC;"
        .format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        if row[1] == sys.argv[4]:
            print(row)
    cur.close()
    db.close()
