from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Port(Base):
    __tablename__ = 'ports'

    id = Column(Integer, primary_key=True)
    port_code = Column(String)

    def __repr__(self):
        return f"<Port(id={self.id}, port_code='{self.port_code}')>"