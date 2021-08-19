# Pets adoption api - Backend

Basic API to work as backend of a pet adoption organization system.
Developed with Django and Django Rest Framework.

### Instructions

* Creat and activate a virtual enviroment:   
`$ python -m venv env`   
`$ source env/bin/activate`   

* Install dependencies:
`$ pip install -r requirements.txt`   

* Creat superuser for admin access:   
`$ cd src`   
`$ python manage.py createsuperuser --email admin@example.com --username admin`   

* Run application:
`$ python -m manage.py runserver`   

### Tests   

* Admin section:   
`127.0.0.1:8000/admin/`   

* API(list all pets - GET, POST):   
`127.0.0.1:8000/api/v1/pets`   

* List specific pet (PUT, DELETE):   
`127.0.0.1:8000/api/v1/pets/<id>`   

* Run automated tests (tests.py):
`$ python -m manage.py test`   

### License   
[MIT](https://choosealicense.com/licenses/mit/)
