#!/usr/bin/python3
"""
Prints all City objects from the database, sorted by state name
"""
import sys
from model_state import Base, State
from model_city import City
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

    # Query all City objects, sorted by state name
    cities = session.query(City).order_by(State.name).all()

    # Print city details
    for city in cities:
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))

    # Close session
    session.close()
