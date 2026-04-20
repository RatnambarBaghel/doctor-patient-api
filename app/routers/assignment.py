from fastapi import APIRouter, HTTPException, Depends
from app.schemas.assignment import AssignmentCreate, AssignmentResponse
from app.database.fake_db import Assignments, Doctors, Patients
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.assignment import Assignment
from app.models.patient import Patient
from app.models.doctor import Doctor
from typing import List


router = APIRouter(prefix="/assignments", tags=["Assignments"])

@router.get("/")
def get_all_assignments(db: Session = Depends(get_db)):

    assignments = db.query(Assignment).all()

    return [
        {
            "assignment_id": a.id,
            "doctor": a.doctor.name,
            "patient": a.patient.name,
            "status": a.status
        }
        for a in assignments
    ]

# Assign a Patient to a Doctor

# @router.post("/", response_model=AssignmentResponse)
# def assign_patient(data: AssignmentCreate):

#     # check doctor exists
#     doctor = next((d for d in Doctors if d["id"] == data.doctor_id), None)
#     if not doctor:
#         raise HTTPException(status_code=404, detail="Doctor not found")

#     # check patient exists and active
#     patient = next(
#         (p for p in Patients if p["id"] == data.patient_id and p["status"] == "active"),
#         None
#     )
#     if not patient:
#         raise HTTPException(status_code=404, detail="Patient not found or inactive")

#     # 🔥 NEW: check duplicate assignment
#     existing = next(
#         (
#             a for a in Assignments
#             if a["doctor_id"] == data.doctor_id
#             and a["patient_id"] == data.patient_id
#             and a["status"] == "active"
#         ),
#         None
#     )

#     if existing:
#         raise HTTPException(
#             status_code=400,
#             detail="Patient already assigned to this doctor"
#         )

#     # create assignment
#     assignment = {
#         "id": len(Assignments) + 1,
#         "doctor_id": data.doctor_id,
#         "patient_id": data.patient_id,
#         "status": "active"
#     }

#     Assignments.append(assignment)
#     return assignment

@router.post("/", response_model=AssignmentResponse)
def assign_patient(data: AssignmentCreate, db: Session = Depends(get_db)):

    #  check doctor exists
    doctor = db.query(Doctor).filter(Doctor.id == data.doctor_id).first()
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    #  check patient exists & active
    patient = db.query(Patient).filter(
        Patient.id == data.patient_id,
        Patient.status == "active"
    ).first()

    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found or inactive")

    #  prevent duplicate assignment
    existing = db.query(Assignment).filter(
        Assignment.doctor_id == data.doctor_id,
        Assignment.patient_id == data.patient_id,
        Assignment.status == "active"
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Already assigned")

    #  create assignment
    new_assignment = Assignment(
        doctor_id=data.doctor_id,
        patient_id=data.patient_id,
        status="active"
    )

    db.add(new_assignment)
    db.commit()
    db.refresh(new_assignment)

    return new_assignment

# Get All active patients for a doctor
# @router.get("/doctor/{doctor_id}")
# def get_doctor_patients(doctor_id : int):

#     result = []

#     for a in Assignments:
#         if a["doctor_id"] == doctor_id and a["status"] == "active":

#             # 🔍 find patient details
#             patient = next(
#                 (p for p in Patients if p["id"] == a["patient_id"] and p["status"] == "active"),
#                 None
#             )

#             if patient:
#                 patient_data = patient.copy()
#                 patient_data.pop("password", None)  # remove password

#                 result.append({
#                     "assignment_id": a["id"],
#                     "doctor_id": doctor_id,
#                     "patient": patient_data,
#                     "status": a["status"]
#                 })

#     return result

# @router.get("/doctor/{doctor_id}")
# def get_doctor_patients(doctor_id: int, db: Session = Depends(get_db)):

#     assignments = db.query(Assignment).filter(
#         Assignment.doctor_id == doctor_id,
#         Assignment.status == "active"
#     ).all()

#     result = []

#     for a in assignments:
#         patient = db.query(Patient).filter(
#             Patient.id == a.patient_id,
#             Patient.status == "active"
#         ).first()

#         if patient:
#             result.append({
#                 "assignment_id": a.id,
#                 "patient": patient
#             })

#     return result

@router.get("/doctor/{doctor_id}")
def get_doctor_patients(doctor_id: int, db: Session = Depends(get_db)):

    assignments = db.query(Assignment).filter(
        Assignment.doctor_id == doctor_id,
        Assignment.status == "active"
    ).all()

    return [
        {
            "assignment_id": a.id,
            "patient": {
                "id": a.patient.id,
                "name": a.patient.name,
                "age": a.patient.age,
                "gender": a.patient.gender
            }
        }
        for a in assignments
    ]

# Discharge a patient from a doctor
# @router.post("/discharge/{assignment_id}")
# def discharge_patient(assignment_id: int):
#     assignment = next((a for a in Assignments if a["id"] == assignment_id), None)

#     if not assignment:
#         raise HTTPException(status_code=404, detail="Assignment not found")
    
#     assignment["status"] = "discharged"
#     return {"message": "Patient discharged successfully"}
@router.put("/discharge/{assignment_id}")
def discharge_patient(assignment_id: int, db: Session = Depends(get_db)):

    assignment = db.query(Assignment).filter(
        Assignment.id == assignment_id
    ).first()

    if not assignment:
        raise HTTPException(status_code=404, detail="Assignment not found")

    assignment.status = "discharged"
    db.commit()

    return {"message": "Patient discharged"}

@router.delete("/{assignment_id}")
def delete_assignment(assignment_id: int):

    for i, a in enumerate(Assignments):
        if a["id"] == assignment_id:
            deleted = Assignments.pop(i)
            return {"message": "Assignment deleted", "data": deleted}

    raise HTTPException(status_code=404, detail="Assignment not found")