install:
	pip install -r requirements.txt

migrate:
	python manage.py migrate

collect-static-file:
	python manage.py collectstatic

run:
	python manage.py runserver
