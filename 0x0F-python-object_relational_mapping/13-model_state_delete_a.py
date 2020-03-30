#!/usr/bin/python3
""" Write a script that deletes all State """
from sqlalchemy import func
import sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy import text


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
    _filter = State.name.like(func.binary('%a%'))
    session.query(State).filter(_filter).delete(synchronize_session='fetch')
    # confirm the change
    session.commit()
    session.close()
