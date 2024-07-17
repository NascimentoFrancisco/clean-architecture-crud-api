# syntax=docker/dockerfile:1

FROM python:3.12

WORKDIR /app

COPY requirements.txt requirements.txt
RUN apt-get update
RUN apt-get install -y redis-server
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "run.py"]
