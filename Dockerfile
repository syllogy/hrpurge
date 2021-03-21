FROM python:3.9.2-slim-buster

RUN pip install -U pip setuptools

WORKDIR /tmp

COPY . .

RUN pip install --no-cache-dir .

RUN pip install -r requirements.txt

CMD [ "hrpurge" ]
