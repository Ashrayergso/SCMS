from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class ShipJobAmounts(Base):
    __tablename__ = 'ship_job_amounts'

    ship_job_key = Column(Integer, primary_key=True)
    ship_code = Column(String, ForeignKey('ships.ship_code'))

    ship = relationship("Ships", back_populates="ship_job_amounts")

    def __init__(self, ship_job_key, ship_code):
        self.ship_job_key = ship_job_key
        self.ship_code = ship_code