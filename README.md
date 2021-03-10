# Soup for Thought Clicker App

A _clicker app_ to record the demand for the [Bristol Soup Run
Trust](https://www.bristolsoupruntrust.org.uk/).

This project was initiated at the social hackathon arranged by Bristol City 
Council on 8/11/19-10/11/19.

Contributors:

  - Charlotte Bermingham
  - Kamran Soomro
  - James Thomas

## Requirements

This project requires Python 3 (version to be confirmed).

The web app uses [Django 3.0](https://docs.djangoproject.com/en/3.0/), which is
supported until April 2021. The next long term support (LTS) version of Django
will be 3.2 LTS, scheduled to be released in April 2021, and supported until
April 2024.

The dashboard uses [Pandas](https://pandas.pydata.org/) and [Plotly by
Dash](https://dash.plotly.com/) (versions need to be confirmed).

## Web App Quickstart

It's best to install the required packages into an isolated virtual environment.
If you don't have a preferred way of doing this, then use:

    $ python -m venv env

Followed by:

    $ . env/bin/activate

to activate your virtual environment. You will need to repeat this activation
step each time you come back to your project.

You can then install the required packages, create the required tables in a
development SQLite database, and create a superuser for you to use:

    $ pip install --upgrade -r requirements.txt
    $ python manage.py migrate
    $ python manage.py createsuperuser

You can then run the Django development server using the manage.py script:

    $ python manage.py runserver

## TODOs

- [x] Added responsive menu
- [x] Added automation location retrieval.
- [ ] Currently location retrieval requires an HTTPs connection. Look into
      possible solutions.
