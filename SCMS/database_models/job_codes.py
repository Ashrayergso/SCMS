from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class JobCodes(Base):
    __tablename__ = 'job_codes'

    id = Column(Integer, primary_key=True)
    job_code = Column(String)

    def __repr__(self):
        return f"<JobCodes(id={self.id}, job_code='{self.job_code}')>"