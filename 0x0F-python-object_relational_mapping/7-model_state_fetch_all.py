#!/usr/bin/python3
"""
Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create engine to connect to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create tables
    Base.metadata.create_all(engine)

    # Create session class
    Session = sessionmaker(bind=engine)

    # Create session
    session = Session()

    # Query and print all instances of State ordered by id
    for instance in session.query(State).order_by(State.id):
        print(instance.id, instance.name, sep=": ")

    # Close session
    session.close()
