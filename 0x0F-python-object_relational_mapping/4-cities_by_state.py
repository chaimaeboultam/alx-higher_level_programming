#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Establish a connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # Create a cursor object to execute SQL queries
    cur = db.cursor()

    # Execute SQL query to select cities and their respective states
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                ORDER BY cities.id ASC")

    # Fetch all rows
    rows = cur.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Clean up process
    cur.close()
    db.close()

