from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CrewMember(Base):
    __tablename__ = 'crew_members'

    crew_id = Column(Integer, primary_key=True)
    crew_name = Column(String)
    contract_duration = Column(Integer)
    vacation_status = Column(String)
    availability = Column(String)
    assigned_ship = Column(String)
    assigned_position = Column(String)

    def __repr__(self):
        return f"<CrewMember(crew_id={self.crew_id}, crew_name={self.crew_name})>"