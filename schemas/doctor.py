from pydantic import BaseModel, Field
from typing import Optional, List


class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str
    house_number: str

class Contact(BaseModel):
    phone: Optional[str] = None
    email: Optional[str] = None

class DoctorCreate(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    specialization: str
    experience: int = Field(ge=0)
    address : Optional[Address] = None
    contact: Optional[Contact] = None
    password: str = Field(min_length=8)

class DoctorResponse(BaseModel):
    id: int
    name: str
    specialization: str
    experience: int
    contact: Optional[Contact] = None