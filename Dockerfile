FROM python:3.7

ARG GUNICORN_HOST
ARG GUNICORN_PORT
ARG GUNICORN_WORKERS
ARG GUNICORN_TIMEOUT

ENV PYTHONPATH=/app/\
    PYTHONUNBUFFERED=1\
    GUNICORN_HOST=${GUNICORN_HOST:-0.0.0.0}\
    GUNICORN_PORT=${GUNICORN_PORT:-80}\
    GUNICORN_WORKERS=${GUNICORN_WORKERS:-4}\
    GUNICORN_TIMEOUT=${GUNICORN_TIMEOUT:-30}

RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip install -r requirements.txt

EXPOSE 80
# will be changed to name of app when using this template
CMD gunicorn -b ${GUNICORN_HOST}:${GUNICORN_PORT} --workers ${GUNICORN_WORKERS} app.app:app --reload
