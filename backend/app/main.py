from fastapi import FastAPI
from .database import engine
from .model import models
from .api.endpoints.v1 import routes

# Create Tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Attendance Management API"
)

# Include Routes
app.include_router(routes.router)


@app.get("/")
def home():
    return {
        "message": "Attendance Management API Running"
    }