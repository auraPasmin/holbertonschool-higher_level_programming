#!/usr/bin/python3
# class state
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    """
    class City
    """

    __tablename__ = 'cities'
    id = Column(
            Integer,
            primary_key=True,
            unique=True,
            nullable=False,
            autoincrement="auto"
         )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
