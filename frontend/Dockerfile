FROM python:3.12-slim
WORKDIR /app
RUN pip install --no-cache-dir django requests
COPY . .
RUN python manage.py migrate
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]