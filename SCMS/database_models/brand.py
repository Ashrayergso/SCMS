from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Brand(Base):
    __tablename__ = 'brands'

    id = Column(Integer, primary_key=True)
    brand_name = Column(String)

    def __repr__(self):
        return f"<Brand(id={self.id}, brand_name={self.brand_name})>"