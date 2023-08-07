from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class DispositionSchedule(Base):
    __tablename__ = 'disposition_schedule'

    id = Column(Integer, primary_key=True)
    crew_id = Column(Integer, ForeignKey('crew_members.crew_id'))
    ship_code = Column(String, ForeignKey('ships.ship_code'))

    crew_member = relationship("CrewMember", back_populates="disposition_schedules")
    ship = relationship("Ship", back_populates="disposition_schedules")

    def __init__(self, crew_id, ship_code):
        self.crew_id = crew_id
        self.ship_code = ship_code