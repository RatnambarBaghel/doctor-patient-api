from fastapi import APIRouter, HTTPException, Depends
from app.schemas.doctor import DoctorCreate, DoctorResponse
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.doctor import Doctor
from app.database.fake_db import Doctors
from typing import List

router = APIRouter(prefix="/doctors", tags=["Doctors"])

@router.post("/", response_model=DoctorResponse)
def create_doctor(doctor: DoctorCreate, db: Session = Depends(get_db)):
    db_doctor = Doctor(**doctor.model_dump())

    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)

    return db_doctor


@router.get("/", response_model=List[DoctorResponse])
def get_doctors(db: Session = Depends(get_db)):
    return db.query(Doctor).all()

@router.get("/{doctor_id}", response_model=DoctorResponse)
def get_doctor(doctor_id: int, db: Session = Depends(get_db)):

    doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()

    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    return doctor

# @router.delete("/{doctor_id}")
# def delete_doctor(doctor_id: int):

#     for i, d in enumerate(Doctors):
#         if d["id"] == doctor_id:
#             deleted = Doctors.pop(i)
#             return {"message": "Doctor deleted", "data": deleted}

#     raise HTTPException(status_code=404, detail="Doctor not found")
@router.delete("/{doctor_id}")
def delete_doctor(doctor_id: int, db: Session = Depends(get_db)):

    doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()

    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    db.delete(doctor)   # remove from DB
    db.commit()

    return {"message": "Doctor deleted"}