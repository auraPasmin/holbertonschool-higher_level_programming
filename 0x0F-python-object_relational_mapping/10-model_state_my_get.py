#!/usr/bin/python3
"""Write a script that prints the State object
with the name passed as argument from the database"""

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
    # get the data - there are objects
    records = session.query(State).filter_by(name=sys.argv[4]).all()
    if not records:
            print("Not found")
    for row in records:
        print("{}".format(row.id))
    session.close()
