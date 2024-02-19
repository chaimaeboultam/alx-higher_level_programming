#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
from sys import argv

# The code should not be executed when imported
if __name__ == '__main__':

    # Make a connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # It gives us the ability to have multiple separate working environments
    # through the same connection to the database.
    cur = db.cursor()

    # Execute the SQL query to select all states and order them by id
    cur.execute("SELECT * FROM states ORDER BY id")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Clean up process
    cur.close()
    db.close()

