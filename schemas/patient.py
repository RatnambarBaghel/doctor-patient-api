from pydantic import BaseModel, Field
from typing import Optional, List

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str
    house_number: str

class Contact(BaseModel):
    email: str
    phone_number: str

class MedicalHistory(BaseModel):
    diseases: List[str]
    allergies: List[str]
    medications: List[str]

class PatientCreate(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    age: int = Field(gt=0, lt=110)
    gender: str
    contact: Optional[Contact] = None
    address: Optional[Address] = None
    medical_history: Optional[MedicalHistory] = None
    password: str = Field(min_length=8)

class PatientResponse(BaseModel):
    id: int
    name: str
    age: int
    gender: str
    contact: Optional[Contact] = None
    address: Optional[Address] = None
    medical_history: Optional[MedicalHistory] = None