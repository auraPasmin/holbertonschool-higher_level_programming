#!/usr/bin/python3
# class state state
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """
    class State
    """

    __tablename__ = 'states'
    id = Column(
            Integer,
            primary_key=True,
            nullable=False,
            autoincrement="auto"
        )
    name = Column(String(128), nullable=False)
