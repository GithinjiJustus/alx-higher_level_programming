#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a' from the database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create engine to connect to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create session class
    Session = sessionmaker(bind=engine)

    # Create session
    session = Session()

    # Query State objects with names containing 'a' and delete them
    states_with_a = session.query(State).filter(State.name.like('%a%')).all()
    for state in states_with_a:
        session.delete(state)

    # Commit the session to the database
    session.commit()

    # Close session
    session.close()
