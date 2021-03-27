#!/usr/bin/python3
"""
write a script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    dbConnect = MySQLdb.connect(host="localhost",
                                port=3306,
                                user=argv[1],
                                passwd=argv[2],
                                db=argv[3])
    cursor = dbConnect.cursor()
    cursor.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC",
                   (argv[4],))
    for states in cursor.fetchall():
        print(states)
    cursor.close()
    dbConnect.close()
