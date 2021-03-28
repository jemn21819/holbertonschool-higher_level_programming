#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa
"""

import sqlalchemy
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":

    engine = create_engine('mysql://{}:{}@{}:{}/{}'.format(
        argv[1], argv[2], 'localhost', 3306, argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    cali = State(name='California')
    sf = City(name='San Francisco')
    cali.cities = [sf]
    session.add(cali)
    session.commit()
    session.close()
