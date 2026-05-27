import requests

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import AttendanceForm, SearchForm


FASTAPI_URL = "http://127.0.0.1:8000"


# ==========================================
# HOME PAGE
# ==========================================

def home(request):

    try:

        response = requests.get(
            f"{FASTAPI_URL}/attendance/"
        )

        records = response.json()

        return render(
            request,
            'attendance/home.html',
            {
                'records': records
            }
        )

    except Exception as e:

        return HttpResponse(
            f"<h2>Backend Connection Error</h2><br>{e}"
        )


# ==========================================
# ADD ATTENDANCE
# ==========================================

def add_attendance(request):

    form = AttendanceForm()

    error = None
    success = None

    if request.method == 'POST':

        form = AttendanceForm(request.POST)

        if form.is_valid():

            payload = {

                "student_name":
                    form.cleaned_data['student_name'],

                "roll_number":
                    form.cleaned_data['roll_number'],

                "date":
                    str(form.cleaned_data['date']),

                "status":
                    form.cleaned_data['status']
            }

            try:

                response = requests.post(
                    f"{FASTAPI_URL}/attendance/",
                    json=payload
                )

                # SUCCESS
                if response.status_code == 200:

                    success = "Attendance Added Successfully"

                    form = AttendanceForm()

                # ERROR FROM BACKEND
                else:

                    data = response.json()

                    error = data.get(
                        'detail',
                        'Something went wrong'
                    )

            except Exception as e:

                error = str(e)

    return render(
        request,
        'attendance/add_attendance.html',
        {
            'form': form,
            'error': error,
            'success': success
        }
    )


# ==========================================
# SEARCH STUDENT
# ==========================================

def search_student(request):

    records = []

    percentage = None

    error = None

    if request.method == 'POST':

        roll_number = request.POST.get(
            'roll_number'
        )

        try:

            # FETCH ATTENDANCE
            response = requests.get(
                f"{FASTAPI_URL}/attendance/{roll_number}"
            )

            if response.status_code == 200:

                records = response.json()

            else:

                error = "Student Not Found"

            # FETCH PERCENTAGE
            percentage_response = requests.get(
                f"{FASTAPI_URL}/attendance/percentage/{roll_number}"
            )

            if percentage_response.status_code == 200:

                percentage = percentage_response.json()

        except Exception as e:

            error = str(e)

    return render(
        request,
        'attendance/search.html',
        {
            'records': records,
            'percentage': percentage,
            'error': error
        }
    )