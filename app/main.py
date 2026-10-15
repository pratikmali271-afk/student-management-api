
from fastapi import FastAPI, Depends, HTTPException, Query, Response
from sqlalchemy.orm import Session

from .database import Base, engine, get_db
from . import models, schemas


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student Management API")


@app.get("/")
def home():
    return {"message": "Welcome to Student Management API"}


# Create a student
@app.post("/students", response_model=schemas.StudentResponse, status_code=201)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    if student.email:
        existing = db.query(models.Student).filter(
            models.Student.email == student.email
        ).first()

        if existing:
            raise HTTPException(status_code=409, detail="Email already exists")

    new_student = models.Student(**student.model_dump())

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student


# Get all students, with an optional course filter
@app.get("/students", response_model=list[schemas.StudentResponse])
def get_students(
    course: str | None = Query(default=None),
    db: Session = Depends(get_db)
):
    query = db.query(models.Student)

    if course:
        query = query.filter(models.Student.course == course)

    return query.order_by(models.Student.id).all()


# Get one student by ID
@app.get("/students/{student_id}", response_model=schemas.StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()

    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return student


# Update a student
@app.patch("/students/{student_id}", response_model=schemas.StudentResponse)
def update_student(
    student_id: int,
    updates: schemas.StudentUpdate,
    db: Session = Depends(get_db)
):
    student = db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()

    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    changes = updates.model_dump(exclude_unset=True)

    if not changes:
        raise HTTPException(
            status_code=400,
            detail="Provide at least one field to update"
        )

    new_email = changes.get("email", student.email)

    if new_email:
        existing = db.query(models.Student).filter(
            models.Student.email == new_email,
            models.Student.id != student_id
        ).first()

        if existing:
            raise HTTPException(status_code=409, detail="Email already exists")

    new_phone = changes.get("phone", student.phone)

    if not new_email and not new_phone:
        raise HTTPException(
            status_code=400,
            detail="A student must have an email or phone number"
        )

    for field, value in changes.items():
        setattr(student, field, value)

    db.commit()
    db.refresh(student)

    return student


# Delete a student
@app.delete("/students/{student_id}", status_code=204)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()

    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    db.delete(student)
    db.commit()

    return Response(status_code=204)
