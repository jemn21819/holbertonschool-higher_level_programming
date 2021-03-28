#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa
"""

import sqlalchemy
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":

    engine = create_engine('mysql://{}:{}@{}:{}/{}'.format(
        argv[1], argv[2], 'localhost', 3306, argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(City, State).join(State)
    for city, state in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
