#!/usr/bin/python3
"""
Module to define the State class and create its corresponding MySQL table.
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    Represents a state in the database.

    Attributes:
        id (int): Unique identifier for the state.
        name (str): Name of the state.
    """
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
