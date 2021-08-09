#!/usr/bin/python3
"""Update the state"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

from sqlalchemy.orm.session import Session
from sqlalchemy.sql import base
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                    argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.id == 2).first()
    state.name = 'New Mexico'
    session.commit()
    session.close()
