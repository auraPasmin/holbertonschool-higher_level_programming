#!/usr/bin/python3
# list all states
import sys
from relationship_state import Base, State
from relationship_city import City
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
    # crate new objects
    new_city = City(name="San Francisco")
    new_state = State(name="California")
    new_state.cities.append(new_city)
    # insert new objects
    session.add(new_state)
    # confirm the change
    session.commit()
    # close session
    session.close()
