from datetime import date, datetime
from enum import Enum

from sqlmodel import Field, SQLModel


class Role(str, Enum):
    doctor = "doctor"
    nurse = "nurse"
    reception = "reception"
    pharmacy = "pharmacy"


class PrescriptionStatus(str, Enum):
    waiting = "waiting"
    given_out = "given_out"
    administered = "administered"


class Ward(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: int | None = Field(default=None, primary_key=True)
    name: str
    username: str = Field(unique=True, index=True)
    email: str | None = None
    hashed_password: str
    role: Role
    ward_id: int | None = Field(default=None, foreign_key="ward.id")


class Patient(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    birth_date: date
    phone: str | None = None


class Allergy(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    patient_id: int = Field(foreign_key="patient.id")
    medicine: str


class Bed(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    ward_id: int = Field(foreign_key="ward.id")
    number: int
    patient_id: int | None = Field(default=None, foreign_key="patient.id")


class Admission(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    patient_id: int = Field(foreign_key="patient.id")
    doctor_id: int = Field(foreign_key="users.id")
    bed_id: int = Field(foreign_key="bed.id")
    admitted_at: datetime
    diagnosis: str | None = None
    discharge_note: str | None = None
    discharged_at: datetime | None = None


class Prescription(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    admission_id: int = Field(foreign_key="admission.id")
    medicine: str
    dose: str
    status: PrescriptionStatus = Field(default=PrescriptionStatus.waiting)
    created_at: datetime


class Vitals(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    admission_id: int = Field(foreign_key="admission.id")
    temperature: float
    blood_pressure: str
    recorded_by: int = Field(foreign_key="users.id")
    recorded_at: datetime