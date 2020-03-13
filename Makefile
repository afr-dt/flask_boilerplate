run:
	python manage.py runserver

shell:
	python manage.py shell

init:
	python manage.py db init	

migrate:
	python manage.py db migrate

upgrade:
	python manage.py db upgrade

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete