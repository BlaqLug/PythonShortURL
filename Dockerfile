FROM python:3.10.5-slim-bullseye

WORKDIR /usr/backend/

ENV PYTHONUNBUFFERED 1

# install python dependencies
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# add app
COPY . .