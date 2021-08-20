FROM python:3.9-alpine as build

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk --no-cache add build-base

RUN pip install pip setuptools --upgrade && \
    pip install fastapi uvicorn[standard]

FROM python:3.9-alpine as publish

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY --from=build /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages/
COPY --from=build /usr/local/bin/ /usr/local/bin/

COPY main.py /app/main.py

ENTRYPOINT [ "uvicorn", "main:app", "--reload", "--host", "0.0.0.0" ]