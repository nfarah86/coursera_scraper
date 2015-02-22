from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
import settings

DeclarativeBase = declarative_base()

def db_connect():
	""" 
	Database connects using db settings: import settings
	sqlalchemy engine instance is returned
	""" 
	return create_engine(URL(**settings.DATABASE))

def create_categories_table(engine):

    DeclarativeBase.metadata.create_all(engine)

class Category(DeclarativeBase):
    """
	Sqlalchemy categories model
	"""
	__tablename__ = "categories"

	id = Column(Integer, primary_key=True)
	organization = Column('organization', String, nullable=False)
	title = Column('title', String, nullable=False)
	author = Column('author', String, nullable=False)
	start_date = Column('start_date', Date(timezone=False), nullable=False)
	duration = Column('duration', Date(timezone=False), nullable=False)






