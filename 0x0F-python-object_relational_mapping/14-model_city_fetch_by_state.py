#!/usr/bin/python3
# list all states
import sys
from model_state import Base, State
from model_city import City
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
    Session = sessionmaker(bind=engine)
    session = Session()
    # get the data - there are objects
    record = session.query(State, City).filter(State.id == City.state_id)
    for row in record:
        print("{}: ({}) {}".format(row[0].name, row[1].id, row[1].name))
    session.close()
