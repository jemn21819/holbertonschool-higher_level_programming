#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa
"""

import sqlalchemy
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
if __name__ == "__main__":

    engine = create_engine('mysql://{}:{}@{}:{}/{}'.format(
        argv[1], argv[2], 'localhost', 3306, argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for city, state in session.query(City, State)\
                              .join(State, State.id == City.state_id)\
                              .order_by(City.id):
        print("{}: {} -> {}".format(city.id, city.name, state.name))
    session.close()
