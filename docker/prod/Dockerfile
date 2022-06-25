FROM python:3.10.4-alpine as builder

WORKDIR /usr/src/app/

COPY requirements.txt .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && \
    apk upgrade && \
    apk add --no-cache --virtual .build-deps postgresql-dev gcc python3-dev musl-dev libpq libffi-dev

RUN pip install --upgrade pip 
RUN pip wheel --no-cache-dir --wheel-dir /usr/src/app/wheels/ -r requirements.txt

RUN apk del .build-deps



FROM python:3.10.4-alpine

RUN apk update

ENV HOME=/home/app/
ENV APP_HOME=/home/app/server/

RUN mkdir -p $HOME
RUN addgroup -S app && adduser -S app -G app

RUN mkdir $APP_HOME
WORKDIR $APP_HOME

COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache /wheels/*

COPY ./ $APP_HOME

RUN chown -R app:app $APP_HOME

USER app

RUN chmod +x $APP_HOME/docker/prod/entrypoint.sh

ENTRYPOINT ["/home/app/server/docker/prod/entrypoint.sh"]
