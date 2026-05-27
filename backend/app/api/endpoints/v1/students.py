from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ....database import get_db
from ....schema import schemas
from ....service import services as crud

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@router.post("/",
             response_model=schemas.StudentResponse)

def add_student(
    student: schemas.StudentCreate,
    db: Session = Depends(get_db)
):

    existing = crud.get_student_by_roll(
        db,
        student.roll_number
    )

    if existing:

        raise HTTPException(
            status_code=400,
            detail="Roll number already exists"
        )

    return crud.create_student(db, student)