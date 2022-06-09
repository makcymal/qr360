FROM python:3.10.4-alpine as builder

WORKDIR /usr/src/app/

COPY requirements.txt .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && \
    apk upgrade

RUN pip install --upgrade pip
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels/ -r requirements.txt



FROM python:3.10.4-alpine

ENV HOME=/home/app/
ENV APP_HOME=/home/app/server/

RUN mkdir -p $HOME
RUN addgroup -S app && adduser -S app -G app

RUN mkdir $APP_HOME
WORKDIR $APP_HOME

COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --no-cache /wheels/*

COPY ./ $APP_HOME

RUN chown -R app:app $APP_HOME

USER app

RUN chmod +x $APP_HOME/docker/prod/entrypoint.sh

ENTRYPOINT ["/home/app/server/docker/prod/entrypoint.sh"]
