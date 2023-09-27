#!/usr/bin/python3
"""Module defines a class State and an instance Base = declarative_base()"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """ Maps a table states in a database.

    __tablename__(str): The name of the mapped table.
    id(int): column to store state ids.
    name(str): column to store state names.
    cities(relationship): the State-City relationship
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
