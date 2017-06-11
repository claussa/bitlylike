# Bitly copy

A copy of bitly write in python with django, django-rest-framework and Json Web Token authentication.

## Installation

**Python 3** and pip3 must be installed on your computer.
Then follow this installation guide :

```
git clone https://github.com/claussa/bitlylike.git
cd bitlylike
pip3 install -r requirement.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

Optionally you can create an admin user with the following command :
```
python3 manage.py createsuperuser
```

Then open your browser and go to <http://localhost:8000/>. 

## Documentation

After launching the server, you will find documentation on the API to <http://localhost:8000/docs>