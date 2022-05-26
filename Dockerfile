FROM python:3.10 AS builder

RUN apt-get update && \
    apt-get install libpq-dev -y && \
    apt-get clean -y

RUN mkdir /app

WORKDIR /app

COPY requirements.txt ./
RUN pip install  --no-cache-dir -r requirements.txt -t .

FROM python:3.10-slim

RUN apt-get update && \
    apt-get install libpq5 -y && \
    apt-get clean -y

COPY --from=builder --chown=65534 /app /app

WORKDIR /app
COPY --chown=65534 . .

USER 65534

RUN python manage.py migrate

CMD [ "python", "-u", "-OO", "manage.py", "runserver",  "0.0.0.0:8080"]
