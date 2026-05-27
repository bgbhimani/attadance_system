from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ....database import get_db
from ....schema import schemas
from ....service import services

router = APIRouter(
    prefix="/attendance",
    tags=["Attendance"]
)


# Add Attendance
@router.post("/", response_model=schemas.AttendanceResponse)
def add_attendance(
    attendance: schemas.AttendanceCreate,
    db: Session = Depends(get_db)
):
    return services.create_attendance(db, attendance)


# Get All Attendance
@router.get("/", response_model=list[schemas.AttendanceResponse])
def fetch_attendance(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return services.get_attendance(db, skip, limit)


# Search Student By Roll Number
@router.get("/{roll_number}",
            response_model=list[schemas.AttendanceResponse])
def search_student(
    roll_number: str,
    db: Session = Depends(get_db)
):

    records = services.get_student_attendance(db, roll_number)

    if not records:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return records


# Attendance Percentage
@router.get("/percentage/{roll_number}",
            response_model=schemas.AttendancePercentage)
def attendance_percentage(
    roll_number: str,
    db: Session = Depends(get_db)
):

    return services.calculate_percentage(db, roll_number)


@router.post("/",
             response_model=schemas.AttendanceResponse)

def add_attendance(
    attendance: schemas.AttendanceCreate,
    db: Session = Depends(get_db)
):

    # CHECK STUDENT EXISTS
    student = crud.get_student_by_roll(
        db,
        attendance.roll_number
    )

    if not student:

        raise HTTPException(
            status_code=404,
            detail="Student Roll Number Does Not Exist"
        )

    return crud.create_attendance(
        db,
        attendance
    )