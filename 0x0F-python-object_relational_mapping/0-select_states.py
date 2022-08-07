#!/usr/bin/python3
""" a script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT id, name FROM states ORDER BY id;")
    for t in cursor.fetchall():
        print(t)
 
    cursor.close()
    db.close()
