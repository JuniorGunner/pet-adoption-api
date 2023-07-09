# 🐾 Pet Adoption API - Backend 

A simple yet powerful API developed to aid pet adoption organizations. It's designed using Django and Django Rest Framework.

## 🧰 Tech Stack

This project is built with the following technologies:

- Python 3.x
- Django
- Django Rest Framework

## 🛠️ Getting Started 

Follow these instructions to get this project up and running on your local machine.

### 🔧 Prerequisites

Ensure you have Python 3.x installed on your machine. You can download it [here](https://www.python.org/downloads/).

### 💻 Installation and Setup

* Create and activate a virtual enviroment:   
```
    $ python -m venv env 
    $ source env/bin/activate
```

* Install dependencies:
`$ pip install -r requirements.txt`   

* Create superuser for admin access:   
```
   $ cd src
   $ python manage.py createsuperuser --email admin@example.com --username admin
```

* Run application:
`$ python -m manage.py runserver`

### 🧪 Testing

1. Admin Section

  * Access the Django admin at `127.0.0.1:8000/admin/`

2. API Endpoints

  * List all pets or create a new pet: `127.0.0.1:8000/api/v1/pets`

  * Access, update, or delete a specific pet: `127.0.0.1:8000/api/v1/pets/<id>`

3. Automated Tests

  * Run the automated tests using:
    `$ python manage.py test`

Happy coding! 🐾


+++
# Pets adoption api - Backend

Basic API to work as backend of a pet adoption organization system.
Developed with Django and Django Rest Framework.

### Instructions

* Create and activate a virtual enviroment:   
`$ python -m venv env`   
`$ source env/bin/activate`   

* Install dependencies:
`$ pip install -r requirements.txt`   

* Create superuser for admin access:   
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
