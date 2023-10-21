FROM ubuntu:22.04
LABEL maintainer="basheerkomassery@gmail.com"

# Update packages to install dependencies for PostgreSQL.
# Refer to the documentation for the Ubuntu image on Docker Hub.
RUN apt-get update && apt-get install -y locales && \
    rm -rf /var/lib/apt/lists/* && \
    localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8

ENV LANG en_US.utf8

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8001

ARG DEV=true

RUN apt-get update && \
    # We specifically require Python 3.10 for this Dockerfile to be compatible with GDAL.
    # At present, Ubuntu Jammy exclusively supports GDAL version 3.4.1.
    apt-get install -y python3.10 python3-venv

ENV PYTHONUNBUFFERED=1

RUN python3 -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install --upgrade setuptools && \
    apt-get install --reinstall -y build-essential && \
    # dependencies for gdal
    apt-get update && \
    apt-get install -y python3-dev libgdal-dev && \
    # Install packages listed in requirements.txt.
    /py/bin/pip install -r /tmp/requirements.txt && \
    # Install packages that are necessary only during the development process.
    if [ $DEV = "true" ]; \
    then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    adduser \
    --disabled-password \
    --no-create-home \
    django-user && \
    mkdir -p /vol/web/media && \
    mkdir -p /vol/web/static && \
    # Restrict root user privileges.
    chown -R django-user:django-user /vol && \
    chmod -R 755 /vol

ENV PATH="/py/bin:$PATH"

USER root
