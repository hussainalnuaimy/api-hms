from datetime import date
from sqlmodel import SQLModel




class PatientCreate(SQLModel):
    name: str
    birth_date: date
    phone: str | None = None
    allergies: list[str] = []




class AdmissionCreate(SQLModel):
    patient_id: int
    doctor_id: int
    bed_id: int

class TextBody(SQLModel):
    text: str




class PrescriptionCreate(SQLModel):
    medicine: str
    dose: str

class VitalsCreate(SQLModel):
    temperature: float
    blood_pressure: str