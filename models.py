from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Job(Base):
    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    company = Column(String)
    location = Column(String)
    salary = Column(Float)

# Create SQLite database
engine = create_engine('sqlite:///data/jobs.db')
Base.metadata.create_all(engine)
