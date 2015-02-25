from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL
import settings
from sqlalchemy import create_engine, Column, Integer, String

DeclarativeBase = declarative_base()
engine = create_engine(URL(**settings.DATABASE), echo=True)

class Category(DeclarativeBase):
    """
    The purpose of this file is to create a table in the db, without manually typing
    the tables in
    Just run: python create_table.py to initalize the db with the table and that's it!
    """
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    organization = Column('organization', String, nullable=True)
    title = Column('title', String, nullable=True)
    author = Column('author', String, nullable=True)
    start_date = Column('start_date', String, nullable=True)
    duration = Column('duration', String, nullable=True)


DeclarativeBase.metadata.create_all(engine)