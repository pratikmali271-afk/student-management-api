
from datetime import date
from pydantic import BaseModel, ConfigDict, EmailStr


class StudentCreate(BaseModel):
    name: str
    date_of_birth: date
    email: EmailStr | None = None
    phone: str | None = None
    course: str | None = None
    address: str | None = None
    enrollment_date: date | None = None


class StudentUpdate(BaseModel):
    name: str | None = None
    date_of_birth: date | None = None
    email: EmailStr | None = None
    phone: str | None = None
    course: str | None = None
    address: str | None = None
    enrollment_date: date | None = None


class StudentResponse(BaseModel):
    id: int
    name: str
    date_of_birth: date
    email: EmailStr | None = None
    phone: str | None = None
    course: str | None = None
    address: str | None = None
    enrollment_date: date | None = None

    model_config = ConfigDict(from_attributes=True)
