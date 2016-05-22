# Microdots Python

Middleware to WSGI applications to capture information from requests send to microservices and send them back to Microdots API.

When gathering the information from the requester it expects a special header: `X-MICRODOT-ORIGIN`. It will tell later the API who requested the microservice.
If the header is not present the request will be ignored.

All requests will be sent in a new thread, to avoid blocking the main process.


## Install

They can be installed (preferably in a [virtualenv][venv]) with:

    pip install -e git+https://github.com/hootsuite-ms-challenge/microdots-python.git#egg=microdots-python

The codebase is compatible with **Python 3.4+**.


## Integrating with your application

This library is compatible with Python WSGI applications. Below are some examples with Django and Flask.

### Flask example

    from flask import Flask
    from microdots import Microdots


    app = Flask(__name__)
    app.wsgi_app = Microdots(app.wsgi_app, 'MICRODOT_SERVER', 'MICRODOT_NAME')


### Django example

    from django.core.wsgi import get_wsgi_application
    from microdots import Microdots

    application = Microdots(get_wsgi_application(), 'MICRODOT_SERVER', 'MICRODOT_NAME')
