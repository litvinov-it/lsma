# Imports
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create url from database
SQLALCHEMY_DATABASE_URL = 'postgresql://danil:123@localhost:5432/lsma'

# Create a database connection
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create local session
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Required line for sqlalchemy
Base = declarative_base()

# Return point to database
def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()