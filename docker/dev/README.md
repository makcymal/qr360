# docker development container
## setup

1. install docker and docker-compose

2. create .env file, example:
```
DEBUG=1
SECRET_KEY=dev
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 0.0.0.0 [::1]

CELERY_BROKER=redis://redis:6379
CELERY_BACKEND=redis://redis:6379

RECAPTCHA_SITE_KEY=change_me
RECAPTCHA_SECRET_KEY=change_me

TELEGRAM_BOT_TOKEN=change_me

PROD_HOST=qr360.tk
```

3. build docker
```
docker-compose build
```

4. run docker
```
docker-compose up
```

captcha: change site_key in front/src/pages/HomePage.vue
tgbot: change bot in front/src/pages/HomePage.vue
