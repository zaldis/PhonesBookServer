run:
	python phonesbook/manage.py runserver

migrate:
	python phonesbook/manage.py migrate

makemigrations:
	python phonesbook/manage.py makemigrations

static:
	python phonesbook/manage.py loadstatic

data: users contacts

users:
	python phonesbook/manage.py loaddata phonesbook/fixtures/users.json

contacts:
	python phonesbook/manage.py loaddata phonesbook/fixtures/contacts.json

