# Microdots Python

Middleware to WSGI applications

## Setup project

    git clone git@bitbucket.org:calangohack/microdots-python.git
    cd microdots-python
    mkvirtualenv microdots-python -p python3
    workon microdots-python
    pip install -r requirements.txt

## Run testes

    python -m unittest

## Flask example

    from flask import Flask
    from microdots import Microdots


    app = Flask(__name__)
    app.wsgi_app = Microdots(app.wsgi_app, 'MICRODOT_SERVER', 'MICRODOT_NAME')

## Django example

    from django.core.wsgi import get_wsgi_application
    from microdots import Microdots

    application = Microdots(get_wsgi_application(), 'MICRODOT_SERVER', 'MICRODOT_NAME')
