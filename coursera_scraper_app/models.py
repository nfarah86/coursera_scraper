from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine, Column, Integer, String
import os
import settings

DeclarativeBase = declarative_base()

# def db_connect():
#     """ 
#     Database connects using db settings: import settings
#     sqlalchemy engine instance is returned
#     """ 
#     return create_engine(URL(**settings.DATABASE))

# def create_categories_table(engine):

#     DeclarativeBase.metadata.create_all(engine)

ENGINE = create_engine(URL(**settings.DATABASE), echo=True)
session = scoped_session(sessionmaker(bind=ENGINE,
                                      autocommit = False,
                                      autoflush = False))


Base = declarative_base() #import Base
Base.query = session.query_property


def connect():
    global ENGINE
    global Session

    ENGINE= create_engine(URL(**settings.DATABASE), echo=True)
    Session = sessionmaker(bind = ENGINE)

    return Session()

def create_categories_db():
    Base.metadata.create_all(bind=Engine)

class Category(DeclarativeBase):
    """
    Sqlalchemy categories model
    """
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    organization = Column('organization', String, nullable=False)
    title = Column('title', String, nullable=False)
    author = Column('author', String, nullable=False)
    start_date = Column('start_date', String, nullable=False)
    duration = Column('duration', String, nullable=False)


################ creating instance of session, initalizing engine ################## 

def main():
    pass


if __name__ == "__main__":
    main()








