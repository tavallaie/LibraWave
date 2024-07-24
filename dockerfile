FROM python:3.12.4-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /code

RUN apt-get update --fix-missing 
RUN apt-get install -y libpq-dev 
RUN apt-get install -qqy postgresql-client

COPY requirements.txt /code/

RUN pip install -r requirements.txt