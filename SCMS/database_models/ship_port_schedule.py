from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class ShipPortSchedule(Base):
    __tablename__ = 'ship_port_schedule'

    id = Column(Integer, primary_key=True)
    ship_code = Column(String, ForeignKey('ships.ship_code'))

    ship = relationship("Ship", back_populates="ship_port_schedules")

    def __init__(self, ship_code):
        self.ship_code = ship_code