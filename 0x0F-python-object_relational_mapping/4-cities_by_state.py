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
    cursor.execute("SELECT cities.id, cities.name, states.name\
    FROM cities INNER JOIN states\
    ON states.id = cities.state_id\
    ORDER BY cities.id ASC")
    for states in cursor.fetchall():
        print(states)
    cursor.close()
    dbConnect.close()
