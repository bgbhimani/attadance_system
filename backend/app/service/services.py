from sqlalchemy.orm import Session
from ..model import models
from ..schema import schemas


# Add Attendance
def create_attendance(db: Session, attendance: schemas.AttendanceCreate):

    db_attendance = models.Attendance(
        student_name=attendance.student_name,
        roll_number=attendance.roll_number,
        date=attendance.date,
        status=attendance.status
    )

    db.add(db_attendance)
    db.commit()
    db.refresh(db_attendance)

    return db_attendance


# Get All Attendance
def get_attendance(db: Session, skip: int = 0, limit: int = 100):

    return db.query(models.Attendance)\
        .offset(skip)\
        .limit(limit)\
        .all()


# Search By Roll Number
def get_student_attendance(db: Session, roll_number: str):

    return db.query(models.Attendance)\
        .filter(models.Attendance.roll_number == roll_number)\
        .all()


# Attendance Percentage
def calculate_percentage(db: Session, roll_number: str):

    records = db.query(models.Attendance)\
        .filter(models.Attendance.roll_number == roll_number)\
        .all()

    total = len(records)

    present = len([
        r for r in records if r.status.lower() == "present"
    ])

    percentage = 0

    if total > 0:
        percentage = (present / total) * 100

    return {
        "roll_number": roll_number,
        "total_classes": total,
        "present_count": present,
        "percentage": round(percentage, 2)
    }
    
# Create Student
def create_student(db: Session, student):

    db_student = models.Student(
        student_name=student.student_name,
        roll_number=student.roll_number
    )

    db.add(db_student)

    db.commit()

    db.refresh(db_student)

    return db_student


# Check Student Exists
def get_student_by_roll(db: Session, roll_number: str):

    return db.query(models.Student)\
        .filter(models.Student.roll_number == roll_number)\
        .first()