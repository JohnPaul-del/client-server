import unittest

from application.server import controller
from application.common.variables import RESPONSE, ERROR, ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME


class TestServerController(unittest.TestCase):
    """
    Test server controller.
    """

    variables_dict = {
        'bad_response': {
            RESPONSE: 400,
            ERROR: 'Bad request',
        },
        'good_response': {RESPONSE: 200},
        'right_message': {
            ACTION: PRESENCE,
            TIME: 1645362000,
            USER: {ACCOUNT_NAME: 'quest'},
        },
        'action_error_message': {
            TIME: 1645362000,
            USER: {ACCOUNT_NAME: 'quest'},
        },
        'incorrect_action_message': {
            ACTION: 'Some action',
            TIME: 1645362000,
            USER: {ACCOUNT_NAME: 'quest'},
        },
        'time_error_message': {
            ACTION: PRESENCE,
            USER: {ACCOUNT_NAME: 'quest'},
        },
        'incorrect_time_message': {
            ACTION: PRESENCE,
            TIME: 'No time here',
            USER: {ACCOUNT_NAME: 'quest'},
        },
        'user_error_message': {
            ACTION: PRESENCE,
            TIME: 1645362000,
            USER: {True: 'Unregistered user'},
        },
        'unregistered_user_error_message': {
            ACTION: PRESENCE,
            TIME: 1645362000,
            USER: {ACCOUNT_NAME: 'Unregistered user'},
        },
    }

    def test_right_message(self):
        """
        Get a right message
        :return: Response status
        """
        self.assertEqual(controller(self.variables_dict['right_message']), self.variables_dict['bad_response'])

    def test_action_error_message(self):
        """
        Action is empty
        :return: Response status
        """
        self.assertEqual(controller(self.variables_dict['action_error_message']), self.variables_dict['bad_response'])

    def test_incorrect_action_message(self):
        """
        Incorrect action message
        :return: Server response
        """
        self.assertEqual(controller(
            self.variables_dict['incorrect_action_message']), self.variables_dict['bad_response'])

    def test_time_error_message(self):
        """
        Time is empty
        :return: server response
        """
        self.assertEqual(controller(self.variables_dict['time_error_message']), self.variables_dict['bad_response'])

    def test_incorrect_action_message(self):
        """
        Incorrect time format
        :return: Server response
        """
        self.assertEqual(controller(
            self.variables_dict['incorrect_action_message']), self.variables_dict['bad_response'])

    def test_user_error_message(self):
        """
        Incorrect user
        :return: Server response
        """
        self.assertEqual(controller(self.variables_dict['user_error_message']), self.variables_dict['bad_response'])

    def test_unregistered_user_error_message(self):
        """
        Unregistered user
        :return: Server response
        """
        self.assertEqual(controller(
            self.variables_dict['unregistered_user_error_message']), self.variables_dict['bad_response'])


if __name__ == '__main__':
    unittest.main()