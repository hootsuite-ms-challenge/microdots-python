import unittest
from unittest.mock import patch

from microdots import Microdots


MICRODOT_NAME = 'Microdot target'
MICRODOT_SERVICE = 'localhost:8000'
MICRODOT_ORIGIN = 'microdot origin'
METHOD = 'GET'
ENDPOINT = 'endpoint'


def start_response(status, response_headers):
    '''start_response fake'''


class MicroDotsTest(unittest.TestCase):

    def setUp(self):
        self.environ = {
            'HTTP_X_MICRODOT_ORIGIN': MICRODOT_ORIGIN,
            'REQUEST_METHOD': METHOD,
            'PATH_INFO': ENDPOINT,
        }

        def app(environ, start_response):
            '''wsgi application fake'''

        self.microdot_app = Microdots(app, MICRODOT_SERVICE, MICRODOT_NAME)

    @patch('microdots.requests.post')
    def test_send_request_if_header_X_MICRODOT_ORIGIN_setted_correctly(self, mock_post_request):
        self.microdot_app(self.environ, start_response)
        data = {
            'origin': MICRODOT_ORIGIN,
            'target': MICRODOT_NAME,
            'method': METHOD,
            'endpoint': ENDPOINT,
        }
        mock_post_request.assert_called_with(MICRODOT_SERVICE, data=data)


if __name__ == '__main__':
    unittest.main()
