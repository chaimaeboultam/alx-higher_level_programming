#!/usr/bin/python3
"""Script that changes the name of a State object from the database"""

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

    # Query the State object with id=2
    state_to_update = session.query(State).filter_by(id=2).first()

    if state_to_update:
        # Update the name of the state
        state_to_update.name = "New Mexico"
        # Commit the session to save the changes to the database
        session.commit()
    else:
        print("State with id=2 not found")

    # Close the session
    session.close()

