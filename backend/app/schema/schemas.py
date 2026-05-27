from pydantic import BaseModel, Field
from datetime import date
from typing import Optional


# Create Attendance
class AttendanceCreate(BaseModel):
    student_name: str = Field(..., min_length=2, max_length=100)
    roll_number: str
    date: date
    status: str

    class Config:
        orm_mode = True


# Response Schema
class AttendanceResponse(BaseModel):
    id: int
    student_name: str
    roll_number: str
    date: date
    status: str

    class Config:
        orm_mode = True


# Attendance Percentage Response
class AttendancePercentage(BaseModel):
    roll_number: str
    total_classes: int
    present_count: int
    percentage: float
    
    
class StudentCreate(BaseModel):

    student_name: str

    roll_number: str


class StudentResponse(BaseModel):

    id: int
    student_name: str
    roll_number: str

    class Config:
        orm_mode = True  