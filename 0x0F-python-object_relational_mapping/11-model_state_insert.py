#!/usr/bin/python3
""" """

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from sqlalchemy import func

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
    # create a new obj
    new_state = State(name="Louisiana")
    # insert the new row
    session.add(new_state)
    # confirm the change
    session.commit()
    # get the id
    records = session.query(State).filter_by(name="Louisiana").all()
    print("{}".format(records[0].id))
    # close session
    session.close()
