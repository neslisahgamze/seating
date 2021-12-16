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

load_data:
	python manage.py loaddata api/fixtures/event.json
	python manage.py loaddata api/fixtures/category.json
	python manage.py loaddata api/fixtures/section.json
	python manage.py loaddata api/fixtures/seat.json

dump_data:
	python manage.py dumpdata api.event > api/fixtures/event.json --indent 4
	python manage.py dumpdata api.people > api/fixtures/category.json --indent 4
	python manage.py dumpdata api.species > api/fixtures/section.json --indent 4
	python manage.py dumpdata api.starship > api/fixtures/seat.json --indent 4

shell:
	docker-compose exec web  /bin/bash