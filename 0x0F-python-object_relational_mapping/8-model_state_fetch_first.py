#!/usr/bin/python3
"""
Prints the first State object from the database
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

    # Query and print the first instance of State
    first_state = session.query(State).first()
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")
    
    # Close session
    session.close()
