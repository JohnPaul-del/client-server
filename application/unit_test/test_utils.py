import json
import unittest
import sys

sys.path.append('..')
from common.utils import send_message, get_message
from common.variables import ENCODING, ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, ERROR


class TestSocket:

    def __init__(self, dict_message):
        self.dict_message = dict_message
        self.controller = None
        self.send_message = None

    def send(self, sending_message):
        json_message = json.dumps(self.dict_message)
        self.controller = json_message.encode(ENCODING)
        self.send_message = sending_message

    def message_receiver(self, max_connections):
        json_message = json.dumps(self.dict_message)
        receiver_controller = json_message.encode(ENCODING)
        return receiver_controller


class TestController(unittest.TestCase):
    message = {
        ACTION:PRESENCE,
        TIME: 1645362000,
        USER: {ACCOUNT_NAME: 'guest'},
    }
    good_response = {RESPONSE: 200}
    bad_response = {
        RESPONSE: 400,
        ERROR: 'Bad request',
    }

    def test_send_message(self):
        """
        Send test message
        :return: Error message
        """

        test_socket = TestSocket(self.message)
        send_message(test_socket, self.message)
        self.assertEqual(test_socket.message_receiver, test_socket.controller)
        self.assertEqual(Exception, send_message)

    def test_get_message(self):
        """
        Test getting message
        :return:
        """

        testing_socket_status_ok = TestSocket(self.good_response)
        testing_socket_status_error = TestSocket(self.bad_response)

        self.assertEqual(get_message(testing_socket_status_ok), self.good_response)
        self.assertEqual(get_message(testing_socket_status_error), self.bad_response)


if __name__ == '__main__':
    unittest.main()
