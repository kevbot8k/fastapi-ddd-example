FROM python:3.11

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

RUN mkdir -p /src
COPY src /src
RUN pip install -e /src
COPY tests/ /tests

WORKDIR /src

CMD uvicorn domain:app