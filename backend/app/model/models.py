from sqlalchemy import Column, Integer, String, Date
from ..database import Base


class Attendance(Base):

    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)

    student_name = Column(String, nullable=False)

    roll_number = Column(String, nullable=False)

    date = Column(Date, nullable=False)

    status = Column(String, nullable=False)
    
    
class Student(Base):

    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)

    student_name = Column(String, nullable=False)

    roll_number = Column(String, unique=True, nullable=False)