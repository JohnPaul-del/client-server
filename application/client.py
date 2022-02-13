import json
import socket
import sys
import time

from common.utils import send_message, get_message
from common.variables import *


def create_message(account='guest'):
    """
    Creating the message for send to server.
    :param account: User name. Default is 'guest'
    :return: Message object
    """

    message = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account,
        },
    }
    return message


def get_response(server_response):
    """
    Read the server response and return status code
    :param server_response: Server response
    :return: Status code
    """

    if RESPONSE in server_response:
        if server_response[RESPONSE] == 200:
            return f'200 OK'
        return f'Error: Server response was {server_response[ERROR]}. Status code: {server_response[RESPONSE]}'
    raise ValueError


def start_client():
    """
    Running client
    :return:
    """
    try:
        if '-a' in sys.argv:
            server_ip_connector = int(sys.argv[sys.argv.index('-a') + 1])
        else:
            server_ip_connector = DEFAULT_IP
    except IndexError:
        print(f'Incorrect IP address after -a key. Please, use correct IP. Example:{DEFAULT_IP}')
        sys.exit(1)

    try:
        if '-p' in sys.argv:
            server_port_connector = int(sys.argv[sys.argv.index('-p') + 1])
            if 1024 < server_port_connector > 65535:
                raise ValueError
        else:
            server_port_connector = DEFAULT_PORT
    except IndexError:
        print(f'Port not specified after -p key. Please specify a valid port. Default port is {DEFAULT_PORT}')
    except ValueError:
        print(f'Port must be in 1024 = 65535 interval. Please specify a valid port. Default port is {DEFAULT_PORT}')
        sys.exit(1)

    server_connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_connect.connect((server_ip_connector, server_port_connector))

    message = create_message()
    send_message(server_connect, message)

    try:
        response = get_response(get_message(server_connect))
        print(response)
    except (ValueError, json.JSONDecodeError):
        print(f'Error: Wrong data or impossible to decode')


if __name__ == '__main__':
    start_client()
