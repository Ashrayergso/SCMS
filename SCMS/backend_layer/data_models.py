from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CrewMembers(Base):
    __tablename__ = 'crew_members'

    crew_id = Column(Integer, primary_key=True)
    crew_name = Column(String)

    disposition_schedule = relationship('DispositionSchedule', back_populates='crew_member')
    training_records = relationship('TrainingRecords', back_populates='crew_member')
    ship_job_amounts = relationship('ShipJobAmounts', back_populates='crew_member')

class DispositionSchedule(Base):
    __tablename__ = 'disposition_schedule'

    id = Column(Integer, primary_key=True)
    crew_id = Column(Integer, ForeignKey('crew_members.crew_id'))
    ship_code = Column(String)

    crew_member = relationship('CrewMembers', back_populates='disposition_schedule')

class TrainingRecords(Base):
    __tablename__ = 'training_records'

    training_id = Column(Integer, primary_key=True)
    training_name = Column(String)
    crew_id = Column(Integer, ForeignKey('crew_members.crew_id'))

    crew_member = relationship('CrewMembers', back_populates='training_records')

class ShipJobAmounts(Base):
    __tablename__ = 'ship_job_amounts'

    ship_job_key = Column(Integer, primary_key=True)
    ship_code = Column(String)
    crew_id = Column(Integer, ForeignKey('crew_members.crew_id'))

    crew_member = relationship('CrewMembers', back_populates='ship_job_amounts')

# Similar classes would be created for Ships, ShipPortSchedule, Ports, Brand, JobCodes, and CrewTrainingRecord