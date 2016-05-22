import threading
import logging

import requests
from requests.exceptions import RequestException


class Microdots:

    def __init__(self, application, microdot_server, microdot_name):
        self.application = application
        self.microdot_name = microdot_name
        self.microdot_server = microdot_server

    def __call__(self, environ, start_response):

        def start_microdot(status, response_headers, exc_info=None):
            try:
                if int(status[0]) in [2, 3]:
                    if environ.get('HTTP_X_MICRODOT_ORIGIN'):
                        data = {
                            'origin': environ.get('HTTP_X_MICRODOT_ORIGIN'),
                            'target': self.microdot_name,
                            'method': environ.get('REQUEST_METHOD'),
                            'endpoint': environ.get('PATH_INFO')
                        }
                        t = threading.Thread(target=self.send_request_to_microdot_server, args=(data, ))
                        t.start()
            except Exception as e:
                logging.error(str(e))
            finally:
                return start_response(status, response_headers, exc_info=None)

        return self.application(environ, start_microdot)


    def send_request_to_microdot_server(self, data):
        try:
            requests.post(self.microdot_server, data=data)
        except RequestException as e:
            logging.error(str(e))
