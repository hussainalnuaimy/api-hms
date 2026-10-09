# HMS API (Team 06)

FastAPI + SQLModel + PostgreSQL. JWT login with roles: reception, doctor, nurse, pharmacy.

## Run locally
1. python -m venv .venv and activate it
2. pip install -r requirements.txt
3. Create .env with DATABASE_URL, SECRET_KEY (see .env.example)
4. Start PostgreSQL (docker compose up -d)
5. python -c "from sqlmodel import SQLModel; from app.database import engine; from app.models import core; SQLModel.metadata.create_all(engine)"
6. python -m app.seed
7. uvicorn app.main:app --reload
8. Open http://127.0.0.1:8000/docs

Demo users (password 1234): doctor1@hms.test, nurse1@hms.test, reception1@hms.test, pharmacy1@hms.test

## Week 1 decisions
- Wards and beds for the demo: Ward A, beds 1-5
- Required vital signs: temperature, blood_pressure
- Prescription statuses: waiting, given_out, administered
- Login: email + password (username also accepted)