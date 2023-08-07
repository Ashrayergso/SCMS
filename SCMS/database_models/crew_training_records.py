from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class CrewTrainingRecords(Base):
    __tablename__ = 'crew_training_records'

    id = Column(Integer, primary_key=True)
    crew_id = Column(Integer, ForeignKey('crew_members.crew_id'))
    training_id = Column(Integer, ForeignKey('training_records.training_id'))

    crew_member = relationship("CrewMembers", back_populates="crew_training_records")
    training_record = relationship("TrainingRecords", back_populates="crew_training_records")

    def __init__(self, crew_id, training_id):
        self.crew_id = crew_id
        self.training_id = training_id