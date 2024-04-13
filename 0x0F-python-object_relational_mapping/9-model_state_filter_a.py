#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a' from the database
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

    # Query and print all states containing 'a'
    states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id)
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    # Close session
    session.close()
