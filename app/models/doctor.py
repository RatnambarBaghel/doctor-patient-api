from sqlalchemy import Column, Integer, String
from app.core.database import Base
from sqlalchemy.orm import relationship

class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    specialization = Column(String(50))
    experience = Column(Integer)
    email = Column(String(100))
    phone = Column(String(15))
    password = Column(String(100))

    assignments = relationship("Assignment", back_populates="doctor")