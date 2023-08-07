from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TrainingRecords(Base):
    __tablename__ = 'training_records'

    training_id = Column(Integer, primary_key=True)
    training_name = Column(String)
    validity = Column(Date)
    crew_id = Column(Integer)

    def __repr__(self):
        return f"<TrainingRecords(training_id={self.training_id}, training_name={self.training_name}, validity={self.validity}, crew_id={self.crew_id})>"