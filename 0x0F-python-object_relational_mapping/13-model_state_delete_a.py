#!/usr/bin/python3
"""Script that deletes all State objects with a name containing the letter 'a'"""

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

    # Query to get all State objects containing the letter 'a'
    states_with_a = session.query(State).filter(State.name.like('%a%')).all()

    if states_with_a:
        for state in states_with_a:
            # Delete the State object
            session.delete(state)
        # Commit the session to save the changes to the database
        session.commit()
    else:
        print("No states found with names containing 'a'")

    # Close the session
    session.close()

