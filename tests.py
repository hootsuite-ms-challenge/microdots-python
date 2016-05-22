import unittest
from unittest.mock import patch

from requests.exceptions import RequestException

from microdots import Microdots


MICRODOT_NAME = 'Microdot target'
MICRODOT_SERVER = 'localhost:8000'
MICRODOT_ORIGIN = 'microdot origin'
METHOD = 'GET'
ENDPOINT = 'endpoint'


def start_response(status, response_headers, exc_info=None):
    '''start_response fake'''


class MicroDotsTest(unittest.TestCase):

    def setUp(self):
        self.environ = {
            'HTTP_X_MICRODOT_ORIGIN': MICRODOT_ORIGIN,
            'REQUEST_METHOD': METHOD,
            'PATH_INFO': ENDPOINT,
        }

        def app(environ, start_response):
            status = '200 OK'
            start_response(status, {})

        self.microdot_app = Microdots(app, MICRODOT_SERVER, MICRODOT_NAME)

    @patch('microdots.requests.post')
    def test_send_request_if_header_X_MICRODOT_ORIGIN_setted_correctly(self, mock_post_request):
        self.microdot_app(self.environ, start_response)
        data = {
            'origin': MICRODOT_ORIGIN,
            'target': MICRODOT_NAME,
            'method': METHOD,
            'endpoint': ENDPOINT,
        }
        mock_post_request.assert_called_with(MICRODOT_SERVER, data=data)

    @patch('microdots.requests.post')
    def test_do_not_send_request_if_header_X_MICRODOT_ORIGIN_it_was_not_set(self, mock_post_request):
        self.environ['HTTP_X_MICRODOT_ORIGIN'] = None
        self.microdot_app(self.environ, start_response)
        mock_post_request.assert_not_called()

    @patch('microdots.logging.error')
    @patch('microdots.requests.post')
    def test_handle_exceptions_correctly_when_sending_request(self, mock_post_request, mock_error_logging):
        mock_post_request.side_effect = RequestException('error')
        self.microdot_app(self.environ, start_response)
        mock_error_logging.assert_called_with('error')

    @patch('microdots.requests.post')
    def test_do_not_send_request_when_response_fail(self, mock_post_request):
        def app(environ, start_response):
            status = '400'
            start_response(status, {})

        microdot_app = Microdots(app, MICRODOT_SERVER, MICRODOT_NAME)
        microdot_app(self.environ, start_response)
        mock_post_request.assert_not_called()

    @patch('microdots.logging.error')
    def test_handle_exceptions_correctly_when_checking_status(self, mock_error_logging):
        def app(environ, start_response):
            status = None
            start_response(status, {})

        microdot_app = Microdots(app, MICRODOT_SERVER, MICRODOT_NAME)
        microdot_app(self.environ, start_response)
        assert mock_error_logging.called


if __name__ == '__main__':
    unittest.main()
