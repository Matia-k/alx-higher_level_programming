#!/usr/bin/python3
"""Module defines a class 'City' """
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """ Maps a table 'cities' in a given database.

    __tablename__(str): The name of the mapped table.
    id(int): column to store the ids of cities.
    name(str): column to store the names if cities.
    state_id(int): column to store the state ids.i
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State")
