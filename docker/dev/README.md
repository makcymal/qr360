# docker development container
## setup

1. install docker and docker-compose

2. create .env file, example:
```
DEBUG=1
SECRET_KEY=django-insecure-v%n%urhg#$3i9ofm-6-6_dgy@r=sk^dnz2fft(=$nc0x+-usl1
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 0.0.0.0 [::1]
CELERY_BROKER=redis://redis:6379
CELERY_BACKEND=redis://redis:6379
```

3. build docker
```
docker-compose build
```

4. run docker
```
docker-compose up
```
