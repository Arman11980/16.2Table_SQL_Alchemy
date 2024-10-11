from sqlalchemy import creat_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = creat_engine('sqlite:///taskmanager.db', echo= True)

SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass