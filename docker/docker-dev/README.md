# docker development container
## setup

0. create .env file, example:

    'DEBUG=1'

    'SECRET_KEY=dev'

    'DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 0.0.0.0 [::1]'

1. install docker and docker-compose

2. build docker

    ` docker-compose build`

3. run docker

    ' docker-compose up '
