run:
	python3 manage.py runserver
migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate


celery:
	celery -A shop worker -l debug
