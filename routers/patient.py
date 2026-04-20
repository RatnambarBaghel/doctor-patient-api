from fastapi import APIRouter, HTTPException, Depends
from app.schemas.patient import PatientCreate, PatientResponse
from app.database.fake_db import Patients
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.patient import Patient
from typing import List

router = APIRouter(prefix="/patients", tags=["Patients"])

@router.post("/", response_model=PatientResponse)
def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    
    db_patient = Patient(**patient.model_dump())  # convert schema → model

    db.add(db_patient)     # add to DB
    db.commit()            # save
    db.refresh(db_patient) # get updated data (like ID)

    return db_patient

@router.get("/", response_model=list[PatientResponse])
def get_patients(db: Session = Depends(get_db)):

    patients = db.query(Patient).filter(Patient.status == "active").all()

    return patients

@router.get("/{patient_id}", response_model=PatientResponse)
def get_patients(patient_id: int,db: Session = Depends(get_db)):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()

    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    return patient

@router.delete("/{patient_id}")
def delete_patient(patient_id: int, db: Session = Depends(get_db)):

    patient = db.query(Patient).filter(Patient.id == patient_id).first()

    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    patient.status = "inactive"
    db.commit()

    return {"message": "Patient deactivated"}