#!/usr/bin/python3
"""
Module that contains class definition for City
"""

from model_state import State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """MySQL table cities"""
    __tablename__ = 'cities'
    id = Column(
        Integer, primary_key=True, autoincrement=True,
        unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
