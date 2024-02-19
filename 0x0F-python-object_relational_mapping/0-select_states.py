#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""
import MySqldb
from sys imort argv

#the code should not be executed when it imported
if __name__ == '__main__':

    #make a connection with MySql server
    db = MySqldb.connect(host = "localhost", port = 3306, user = argv[1],
                         passrd = argv[2], db = argv[3])

     # It gives us the ability to have multiple seperate working environments
     # through the same connection to the database.
     cur = db.cursor()
     cur.execute("SELECT *FROM states OREDERED BY id")

     rows = cur.fetchall()
     for i in rows:
         print(i)

     #clean up process
     cur.close()
     db.close()
