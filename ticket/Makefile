build:
	docker-compose build

up:
	docker-compose up

start: build up

down:
	docker-compose down

createsuperuser:
	docker-compose run --rm web python manage.py createsuperuser

migrate:
	docker-compose run --rm web python manage.py migrate

makemigrations:
	docker-compose run --rm web python manage.py makemigrations

test:
	docker-compose run --rm web python manage.py test api.tests