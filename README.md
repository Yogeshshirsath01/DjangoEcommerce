# DjangoEcommerce
 Ecommerce website with Django and HTML

## Demo
https://django-ecommerce-shop.herokuapp.com/

### Main features

* Example app with custom user model

* Bootstrap static files included

* Use can register and login

* Procfile for easy deployments

* Separated requirements files

* SQLite by default if no env variable is set


# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/Yogeshshirsath01/DjangoEcommerce
    $ cd {{ DjangoEcommerce }}
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements.txt
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver
