#!/usr/bin/python3
"""Show states in database"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    curs.execute("SELECT id, name FROM states \
                WHERE name = '{:s}' ORDER BY id;".format(sys.argv[4]))
    for t in curs.fetchall():
        if sys.argv[4] == t[1]:
            print(t)
