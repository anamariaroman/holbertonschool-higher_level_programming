#!/usr/bin/python3
"""Add the new state. """

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
    nuevo = State(name='Louisiana')
    session.add(nuevo)
    session.commit()
    print(nuevo.id)
    session.close()
