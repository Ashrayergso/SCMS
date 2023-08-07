from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CrewMembers(Base):
    __tablename__ = 'crew_members'

    crew_id = Column(Integer, primary_key=True)
    crew_name = Column(String)

class DispositionSchedule(Base):
    __tablename__ = 'disposition_schedule'

    id = Column(Integer, primary_key=True)
    crew_id = Column(Integer, ForeignKey('crew_members.crew_id'))
    ship_code = Column(String)

class TrainingRecords(Base):
    __tablename__ = 'training_records'

    training_id = Column(Integer, primary_key=True)
    training_name = Column(String)

class ShipJobAmounts(Base):
    __tablename__ = 'ship_job_amounts'

    ship_job_key = Column(Integer, primary_key=True)
    ship_code = Column(String)

class Ships(Base):
    __tablename__ = 'ships'

    ship_id = Column(Integer, primary_key=True)
    ship_name = Column(String)

class ShipPortSchedule(Base):
    __tablename__ = 'ship_port_schedule'

    id = Column(Integer, primary_key=True)
    ship_code = Column(String)

class Ports(Base):
    __tablename__ = 'ports'

    id = Column(Integer, primary_key=True)
    port_code = Column(String)

class Brand(Base):
    __tablename__ = 'brand'

    id = Column(Integer, primary_key=True)
    brand_name = Column(String)

class JobCodes(Base):
    __tablename__ = 'job_codes'

    id = Column(Integer, primary_key=True)
    job_code = Column(String)

class CrewTrainingRecords(Base):
    __tablename__ = 'crew_training_records'

    id = Column(Integer, primary_key=True)
    crew_id = Column(Integer, ForeignKey('crew_members.crew_id'))

engine = create_engine('sqlite:///scms.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()