# docker development container
## setup

1. buid vue
```
yarn build
```

2. install docker and docker-compose

3. create .env file, example:
```
DEBUG=0
SECRET_KEY=change_me
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=postgresql
SQL_USER=user
SQL_PASSWORD=password
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres

POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=postgresql

CELERY_BROKER=redis://redis:6379
CELERY_BACKEND=redis://redis:6379
TGBOT=<bot_token>

```

4. build docker
```
docker-compose build
```

5. run docker
```
docker-compose up
```
