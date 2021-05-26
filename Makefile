make lint:
	flake8 --exclude=*/migrations/*,*/views.py,./pontos_turisticos/*,./manage.py --count
make test:
	python manage.py test -v2
make fixtures:
	python manage.py loaddata */fixtures/*