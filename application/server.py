import json
import socket
import sys
from logging import getLogger

import application.log_config.server_log_config
from common.utils import get_message, send_message
from common.variables import *
from decors import log

LOGGER = getLogger('server')


@log
def controller(message_from_client):
    """
    Check the messages` protocol from client
    :param message_from_client: Message from client
    :return: Code of the controller
    """
    LOGGER.debug(f'Check message from client: {message_from_client}')

    if ACTION in message_from_client and message_from_client[ACTION] == PRESENCE \
            and message_from_client[TIME] and message_from_client[USER][ACCOUNT_NAME] == 'guest':
        return {
            RESPONSE: 200
        }
    return {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }


@log
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
        LOGGER.error('Incorrect IP address after -a key')
        sys.exit(1)

    try:
        if '-p' in sys.argv:
            client_port_connector = int(sys.argv[sys.argv.index('-p') + 1])
            if 1024 < client_port_connector > 65535:
                raise ValueError
        else:
            client_port_connector = DEFAULT_PORT
    except IndexError:
        print(f'Incorrect port number after -p key. Please specify a valid port. Default port is {DEFAULT_PORT}')
        LOGGER.error('Incorrect port number after -p key')
    except ValueError:
        print(f'Port must be in 1024 = 65535 interval. Please specify a valid port. Default port is {DEFAULT_PORT}')
        LOGGER.critical(f'Incorrect port number after -p key. Attempting to connect to port {client_port_connector}')
        sys.exit(1)

    client_connector = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_connector.bind((client_ip_connector, client_port_connector))
    client_connector.listen(MAX_CONNECTIONS)

    while True:
        client, client_ip_address = client_connector.accept()
        LOGGER.info(f'Client connection established on {client_ip_address}')
        try:
            client_message = get_message(client)
            LOGGER.debug(f'Message has been received: {client_message}')
            print(f'Message received: {client_message}\n')
            response = controller(client_message)
            send_message(client, response)
            LOGGER.debug(f'Response to client: {response}')
            client.close()
        except (ValueError, json.JSONDecodeError):
            print(f'Incorrect message received: {client_ip_address}\n')
            LOGGER.error(f'Incorrect message received: {client_ip_address}')
            client.close()


if __name__ == '__main__':
    start_server()
