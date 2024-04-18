#!/usr/bin/python3
"""
Script that creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

   # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create California state with San Francisco city
    newState = State(name='California')
    newCity = City(name='San Francisco')
    newState.cities.append(newCity)

    # Add objects to session and commit
    session.add(newState)
    session.add(newCity)
    session.commit()
