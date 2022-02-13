import json
import socket
import sys

from common.utils import get_message, send_message
from common.variables import *


def controller(message_from_client):
    """
    Check the messages` protocol from client
    :param message_from_client: Message from client
    :return: Code of the controller
    """

    if ACTION in message_from_client and message_from_client[ACTION] == PRESENCE \
            and message_from_client[TIME] and message_from_client[USER][ACCOUNT_NAME] == 'guest':
        return {
            RESPONSE: 200
        }
    return {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }


def start_server():
    """
    Starting the server
    :return: Server
    """

    try:
        if '-a' in sys.argv:
            client_ip_connector = int(sys.argv[sys.argv.index('-a') + 1])
        else:
            client_ip_connector = DEFAULT_IP
    except IndexError:
        print(f'Incorrect IP address after -a key. Please, use correct IP. Example:{DEFAULT_IP}')
        sys.exit(1)

    try:
        if '-p' in sys.argv:
            client_port_connector = int(sys.argv[sys.argv.index('-p') + 1])
            if 1024 < client_port_connector > 65535:
                raise ValueError
        else:
            client_port_connector = DEFAULT_PORT
    except IndexError:
        print(f'Port not specified after -p key. Please specify a valid port. Default port is {DEFAULT_PORT}')
    except ValueError:
        print(f'Port must be in 1024 = 65535 interval. Please specify a valid port. Default port is {DEFAULT_PORT}')
        sys.exit(1)

    client_connector = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_connector.bind((client_ip_connector, client_port_connector))
    client_connector.listen(MAX_CONNECTIONS)

    while True:
        client, client_ip_address = client_connector.accept()
        try:
            client_message = get_message(client)
            print(f'Message received: {client_message}\n')
            response = controller(client_message)
            send_message(client, response)
            client.close()
        except (ValueError, json.JSONDecodeError):
            print(f'Incorrect message received: {client_ip_address}\n')
            client.close()


if __name__ == '__main__':
    start_server()
