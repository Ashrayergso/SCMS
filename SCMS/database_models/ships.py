from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Ships(Base):
    __tablename__ = 'ships'

    ship_id = Column(Integer, primary_key=True)
    ship_name = Column(String)

    def __init__(self, ship_id, ship_name):
        self.ship_id = ship_id
        self.ship_name = ship_name