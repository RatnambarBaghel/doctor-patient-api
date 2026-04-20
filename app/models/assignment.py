from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
# from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
# from app.core.database import Base

class Assignment(Base):
    __tablename__ = "assignments"

    id = Column(Integer, primary_key=True, index=True)
    doctor_id = Column(Integer, ForeignKey("doctors.id"))
    patient_id = Column(Integer, ForeignKey("patients.id"))
    status = Column(String(20), default="active")

    #  relationships
    doctor = relationship("Doctor", back_populates="assignments")
    patient = relationship("Patient", back_populates="assignments")