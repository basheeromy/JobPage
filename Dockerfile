FROM ubuntu:22.04
LABEL maintainer="basheerkomassery@gmail.com"

# update packages for installing dependencies for postgresql
RUN apt-get update && apt-get install -y locales && \
    rm -rf /var/lib/apt/lists/* && \
    localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8

ENV LANG en_US.utf8

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8001

ARG DEV=false

RUN apt-get update && \
    # install python 3 and
    apt-get install -y python3.10 python3-venv

ENV PYTHONUNBUFFERED=1

RUN python3 -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install --upgrade setuptools && \
    apt-get install --reinstall -y build-essential && \
    apt-get update && \
    apt-get install -y python3-dev libgdal-dev && \
    /py/bin/pip install -r /tmp/requirements.txt && \
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
    chown -R django-user:django-user /vol && \
    chmod -R 755 /vol

ENV PATH="/py/bin:$PATH"

USER root
