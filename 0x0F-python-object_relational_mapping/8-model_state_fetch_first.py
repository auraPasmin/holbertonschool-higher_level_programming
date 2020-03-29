#!/usr/bin/python3
"""
    Write a script that prints the first State
    object from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]),
            pool_pre_ping=True
         )
    Base.metadata.create_all(engine)
    # create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # create a Session
    session = Session()
    # get the data - there are objects
    records = session.query(State).first()
    if not records:
            print("Nothing")
    else:
        print("{}: {}".format(records.id, records.name))
    # close session
    session.close()
