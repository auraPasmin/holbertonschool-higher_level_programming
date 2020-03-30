#!/usr/bin/python3
"""
Write a script that changes the name of a
State object from the database
"""

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
    # get the id
    session.query(State).\
        filter_by(id=2).\
        update({State.name: "New Mexico"}, synchronize_session=False)
    # confirm the change
    session.commit()
    # close session
    session.close()
