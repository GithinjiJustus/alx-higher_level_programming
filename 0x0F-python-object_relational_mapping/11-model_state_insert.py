#!/usr/bin/python3
"""
Adds the State object "Louisiana" to the database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create engine to connect to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    # Create session class
    Session = sessionmaker(bind=engine)

    # Create session
    session = Session()

    # Create new State object
    new_state = State(name="Louisiana")

    # Add the new State object to the session
    session.add(new_state)

    # Commit the session to the database
    new_instance = session.query(State).filter_by(name='Louisiana').first()

    # Print the id of the newly added State object
    print(new_state.id)

    # Close session
    session.commit()
