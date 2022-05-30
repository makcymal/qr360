# docker development container
## setup

1. install docker and docker-compose

2. create .env file, example:

    ` DEBUG=1 `

    ` SECRET_KEY=dev `

    ` DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 0.0.0.0 [::1] `

3. build docker

    ` docker-compose build`

4. run docker

    ` docker-compose up `
