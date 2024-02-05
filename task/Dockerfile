# FROM python:3.10
# ENV PYTHONUNBUFFERED=1
# WORKDIR /app
# COPY requirements.txt .
# RUN pip install -r requirements.txt --no-cache-dir
# COPY . .
# CMD ["python", "manage.py", "runserver", "0:8000"]
FROM python:3.10
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/