#!/usr/bin/python3
"""
Changes the name of a State object with id = 2 to "New Mexico"
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

    # Query the State object with id = 2
    new_instance = session.query(State).filter_by(id=2).first()

    # Update the name attribute of the State object
    new_instance.name = 'New Mexico'

    # Commit the session to the database
    session.commit()
