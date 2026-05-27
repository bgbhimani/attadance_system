# Student Attendance Management System

This is a full-stack web application for managing student attendance, built with a FastAPI backend and a Django frontend.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Technology Stack](#technology-stack)
- [Setup and Installation](#setup-and-installation)
  - [Backend (FastAPI)](#backend-fastapi)
  - [Frontend (Django)](#frontend-django)
- [API Endpoints](#api-endpoints)

## Features

-   **Add Attendance:** Mark attendance for students with their name, roll number, date, and status (Present/Absent).
-   **View All Records:** A dashboard to display all attendance records.
-   **Search by Roll Number:** Search for a specific student's attendance history using their roll number.
-   **Attendance Percentage:** Automatically calculates and displays the attendance percentage for a searched student.
-   **Data Visualization:** A pie chart visually represents the present vs. absent ratio for a student.
-   **Decoupled Architecture:** A separate FastAPI backend serves a REST API, consumed by a Django frontend.

## Project Structure

The project is divided into two main directories: `backend` and `frontend`.

```
.
├── backend/      # FastAPI application
│   ├── app/
│   ├── attendance.db
│   └── pyproject.toml
└── frontend/     # Django application
    ├── attendance/
    ├── config/
    ├── manage.py
    └── pyproject.toml
```

## Technology Stack

-   **Backend:**
    -   Python 3.12
    -   FastAPI
    -   SQLAlchemy (ORM)
    -   SQLite (Database)
    -   Uvicorn (ASGI Server)

-   **Frontend:**
    -   Python 3.12
    -   Django
    -   Requests (for API communication)
    -   Chart.js (for data visualization)
    -   HTML5 & CSS3

## Setup and Installation

### Prerequisites

-   Python 3.12 or higher
-   A virtual environment tool like `venv`

### Backend (FastAPI)

1.  **Navigate to the backend directory:**
    ```sh
    cd backend
    ```

2.  **Create and activate a virtual environment:**
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```sh
    pip install -r requirements.txt 
    # Or if you use a tool like `uv`:
    # uv pip install -r requirements.txt
    ```
    *(Note: A `requirements.txt` file can be generated from `pyproject.toml`)*

4.  **Run the FastAPI server:**
    The application is configured to run using an ASGI server like Uvicorn. The main app instance is in `backend/app/main.py`.
    ```sh
    uvicorn app.main:app --reload
    ```
    The backend server will start on `http://127.0.0.1:8000`.

### Frontend (Django)

1.  **Navigate to the frontend directory:**
    ```sh
    cd frontend
    ```

2.  **Create and activate a virtual environment:**
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    # Or if you use a tool like `uv`:
    # uv pip install -r requirements.txt
    ```

4.  **Run database migrations:**
    ```sh
    python manage.py migrate
    ```

5.  **Run the Django development server:**
    ```sh
    python manage.py runserver
    ```
    The frontend will be accessible at `http://127.0.0.1:8000`. Make sure the backend is running on a different port or that you run them one at a time if using the default port for both. For development, you can run the Django server on a different port:
    ```sh
    python manage.py runserver 8001
    ```

## API Endpoints

The FastAPI backend provides the following endpoints, which are consumed by the Django frontend.

| Method | Endpoint                               | Description                                      |
| :----- | :------------------------------------- | :----------------------------------------------- |
| `POST` | `/attendance/`                         | Adds a new attendance record.                    |
| `GET` | `/attendance/`                         | Retrieves a list of all attendance records.      |
| `GET`  | `/attendance/{roll_number}`            | Searches for attendance records by roll number.  |
| `GET`  | `/attendance/percentage/{roll_number}` | Calculates attendance percentage for a student.  |