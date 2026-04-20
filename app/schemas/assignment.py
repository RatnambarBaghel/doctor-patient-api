from pydantic import BaseModel

class AssignmentCreate(BaseModel):
    doctor_id: int
    patient_id: int

class AssignmentResponse(BaseModel):
    id: int
    doctor_id: int
    patient_id: int
    status: str   # active / discharged