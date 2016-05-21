import threading

import requests


class Microdots:

    def __init__(self, application, microdot_service, microdot_name):
        self.application = application
        self.microdot_name = microdot_name
        self.microdot_service = microdot_service

    def __call__(self, environ, start_response):
        data = {
            'origin': environ.get('HTTP_X_MICRODOT_ORIGIN'),
            'target': self.microdot_name,
            'method': environ.get('REQUEST_METHOD'),
            'endpoint': environ.get('PATH_INFO')
        }
        t = threading.Thread(target=self.send_request_to_microdot_service, args=(data, ))
        t.start()
        return self.application(environ, start_response)


    def send_request_to_microdot_service(self, data):
        requests.post(self.microdot_service, data=data)
