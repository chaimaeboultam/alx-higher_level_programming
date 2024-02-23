#!/usr/bin/python3
"""Script that adds the State object "Louisiana" to the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1:]

    # Create engine to connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)

    # Create Session class bound to engine
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Create the State object
    new_state = State(name="Louisiana")

    # Add the State object to the session
    session.add(new_state)

    # Commit the session to save the changes to the database
    session.commit()

    # Print the new state's ID
    print(new_state.id)

    # Close the session
    session.close()

