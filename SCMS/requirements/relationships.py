from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from database_models import Base, CrewMembers, DispositionSchedule, TrainingRecords, ShipJobAmounts, Ships, ShipPortSchedule, Ports, Brand, JobCodes, CrewTrainingRecords

class CrewMembers(Base):
    __tablename__ = 'crew_members'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    disposition_schedule = relationship("DispositionSchedule", back_populates="crew_member")
    training_records = relationship("TrainingRecords", back_populates="crew_member")
    ship_job_amounts = relationship("ShipJobAmounts", back_populates="crew_member")
    crew_training_records = relationship("CrewTrainingRecords", back_populates="crew_member")

class DispositionSchedule(Base):
    __tablename__ = 'disposition_schedule'
    id = Column(Integer, primary_key=True)
    crew_id = Column(Integer, ForeignKey('crew_members.id'))
    crew_member = relationship("CrewMembers", back_populates="disposition_schedule")
    ship_code = Column(Integer, ForeignKey('ships.id'))
    ship = relationship("Ships", back_populates="disposition_schedule")

class TrainingRecords(Base):
    __tablename__ = 'training_records'
    id = Column(Integer, primary_key=True)
    crew_id = Column(Integer, ForeignKey('crew_members.id'))
    crew_member = relationship("CrewMembers", back_populates="training_records")

class ShipJobAmounts(Base):
    __tablename__ = 'ship_job_amounts'
    id = Column(Integer, primary_key=True)
    crew_id = Column(Integer, ForeignKey('crew_members.id'))
    crew_member = relationship("CrewMembers", back_populates="ship_job_amounts")
    ship_code = Column(Integer, ForeignKey('ships.id'))
    ship = relationship("Ships", back_populates="ship_job_amounts")

class Ships(Base):
    __tablename__ = 'ships'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    disposition_schedule = relationship("DispositionSchedule", back_populates="ship")
    ship_job_amounts = relationship("ShipJobAmounts", back_populates="ship")
    ship_port_schedule = relationship("ShipPortSchedule", back_populates="ship")

class ShipPortSchedule(Base):
    __tablename__ = 'ship_port_schedule'
    id = Column(Integer, primary_key=True)
    ship_code = Column(Integer, ForeignKey('ships.id'))
    ship = relationship("Ships", back_populates="ship_port_schedule")
    port_code = Column(Integer, ForeignKey('ports.id'))
    port = relationship("Ports", back_populates="ship_port_schedule")

class Ports(Base):
    __tablename__ = 'ports'
    id = Column(Integer, primary_key=True)
    code = Column(String)
    ship_port_schedule = relationship("ShipPortSchedule", back_populates="port")

class Brand(Base):
    __tablename__ = 'brand'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class JobCodes(Base):
    __tablename__ = 'job_codes'
    id = Column(Integer, primary_key=True)
    code = Column(String)

class CrewTrainingRecords(Base):
    __tablename__ = 'crew_training_records'
    id = Column(Integer, primary_key=True)
    crew_id = Column(Integer, ForeignKey('crew_members.id'))
    crew_member = relationship("CrewMembers", back_populates="crew_training_records")