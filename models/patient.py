from sqlalchemy import Column, Integer, String
from app.core.database import Base
from sqlalchemy.orm import relationship

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    age = Column(Integer)
    gender = Column(String(10))
    email = Column(String(100))
    phone = Column(String(15))
    password = Column(String(100))
    status = Column(String(20), default="active")
    assignments = relationship("Assignment", back_populates="patient")