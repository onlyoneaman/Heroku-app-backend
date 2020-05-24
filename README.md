# Python: Getting Started

A barebones Django app, which can easily be deployed to Heroku.

This application supports the [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) article - check it out.

## Running Locally

Make sure you have Python 3.7 [installed locally](http://install.python-guide.org). To push to Heroku, you'll need to install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli), as well as [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

### Intalling Heroku Cli
```sh
$ sudo snap install --classic heroku
```
The above command is for Ubuntu 16+ Users
For other options, visit [here](https://devcenter.heroku.com/articles/heroku-cli)

### Install Postgres
1. Check this [link](https://www.postgresql.org/download/) for instaling Postgres 
```sh
$ sudo su - postgres
$ psql
postgres-# CREATE ROLE your_username WITH LOGIN CREATEDB ENCRYPTED PASSWORD 'your_password';
postgres-# \q
```
TO change a user to superuser
```sh
ALTER USER dell WITH SUPERUSER;
```

### Commands to run heroku app locally
```sh
$ git clone https://github.com/heroku/python-getting-started.git
$ cd python-getting-started

$ python3 -m venv getting-started
$ pip install -r requirements.txt

$ createdb python_getting_started

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
