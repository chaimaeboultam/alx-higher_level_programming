#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N)
from the database
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Establish a connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # Create a cursor object to execute SQL queries
    cur = db.cursor()

    # Execute SQL query to select states starting with 'N'
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")

    # Fetch all matching rows
    rows = cur.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Clean up process
    cur.close()
    db.close()

