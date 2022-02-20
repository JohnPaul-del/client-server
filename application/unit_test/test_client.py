import unittest

from application.client import create_message, get_response
from application.common.variables import RESPONSE, ERROR, TIME, ACTION, PRESENCE, ACCOUNT_NAME, USER


class TestClient(unittest.TestCase):
    """
    Test client
    """

    variables_dict = {
        'good_response': '200. Connected',
        'bad_response': '400. Error',
        'test_request': {
            ACTION: PRESENCE,
            TIME: 1645362000,
            USER: {
                ACCOUNT_NAME: 'quest',
            },
        },
        'good_server_response': {
            RESPONSE: 200
        },
        'bad_server_response': {
            RESPONSE: 400,
            ERROR: 'Connection Failed'
        },
    }

    def test_message(self):
        """
        Testing a request
        :return: connection status
        """

        test_message = create_message()
        test_message[TIME] = 1645362000
        self.assertEqual(test_message, self.variables_dict['test_request'])

    def test_good_response(self):
        """
        Testing successful connection
        :return: Successful connection status
        """

        self.assertEqual(
            get_response(self.variables_dict['good_server_response']),
            self.variables_dict['good_response']
        )

    def test_bad_response(self):
        """
        Testing failed connection
        :return: Failed connection status
        """

        self.assertEqual(
            get_response(self.variables_dict['bad_server_response']),
            self.variables_dict['bad_response']
        )

    def test_server_error_response(self):
        """
        Test server response with error
        :return: Server response
        """

        self.assertRaises(ValueError, get_response, self.variables_dict['bad_server_response'])


if __name__ == '__main__':
    unittest.main()
