FROM python:3.9.2-slim-buster

WORKDIR /app

COPY ./hrpurge ./hrpurge
COPY ./setup.py .
COPY ./requirements.txt .

RUN pip install -e .

CMD [ "hrpurge" ]
