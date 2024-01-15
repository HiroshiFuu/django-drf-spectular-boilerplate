FROM python:3.11 AS base

FROM base AS os-dep
RUN apt-get update -y --fix-missing
RUN apt update -y --fix-missing
RUN apt-get -y install nano
RUN apt-get upgrade -y
ENV PYTHONUNBUFFERED=1
RUN pip install --upgrade pip
ARG CACHEBUST

FROM os-dep AS django-dep
WORKDIR /app/logs
WORKDIR /app/static
WORKDIR /app
ENV PYTHONUNBUFFERED=2
COPY requirements/base.txt /app/
RUN pip install -r ./base.txt
ENV PYTHONUNBUFFERED=3
ARG CACHEBUST

FROM django-dep AS django
COPY core/ /app/core/
COPY configuration/ /app/configuration/
COPY backend/ /app/backend/
COPY manage.py /app/
RUN python3 /app/manage.py collectstatic --noinput
ENV PYTHONUNBUFFERED=4
ARG CACHEBUST

COPY entrypoint.sh bin/entrypoint.sh
RUN chmod +x bin/entrypoint.sh

ENTRYPOINT ["bin/entrypoint.sh"]