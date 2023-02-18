##### Prepare base container
FROM python:3.11-alpine as python-base

ENV PYTHONDONTWRITEBYTECODE 1 \
    PYTHONUNBUFFERED 1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 

RUN apk --no-cache update && \
    apk --no-cache upgrade && \
    pip --no-cache-dir install pip setuptools --upgrade

##### Prepare builder container
FROM python-base as build

RUN apk --no-cache add build-base

RUN pip install fastapi uvicorn[standard]

##### Prepare production image
FROM python-base as publish

WORKDIR /app

COPY --from=build /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/
COPY --from=build /usr/local/bin/ /usr/local/bin/

COPY main.py /app/main.py

ENTRYPOINT [ "uvicorn", "main:app", "--reload", "--host", "0.0.0.0" ]