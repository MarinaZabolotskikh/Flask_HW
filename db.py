import atexit
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session
from sqlalchemy import create_engine
from datetime import datetime

PG_DSN = 'postgresql://app:1234@127.0.0.1:5431/flask_hw'

engine = create_engine(PG_DSN)
#Base = declarative_base(bind=engine)

class Base(DeclarativeBase):
    pass
class AdvertModel(Base):

    __tablename__ = "app_adverts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    heading = Column(String, nullable=False)
    description = Column(String, nullable=False)
    creation_date = Column(DateTime, default=datetime.now())
    owner = Column(String, nullable=False)

Session = Base.metadata.create_all(bind=engine)
#Session = sessionmaker(bind=engine)
atexit.register(engine.dispose)