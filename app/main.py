from fastapi import FastAPI
from app.routers import patient, doctor, assignment
from app.core.database import Base, engine
from app.routers import patient, doctor, assignment

app = FastAPI(
    title="Doctor Patient Management API",
    description="API for managing doctors, patients, and assignments",
    version="1.0.0"
)

app.include_router(patient.router)
app.include_router(doctor.router)
app.include_router(assignment.router)

# connect with DB
Base.metadata.create_all(bind=engine)