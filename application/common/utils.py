import json
from .variables import *


def send_message(socket, message):
    """
    Encoding and send message

    :param socket: Server socket
    :param message: Text message to encode
    :return: Sending encode message
    """

    json_message = json.dumps(message)
    message_coding = json_message.encode(ENCODING)
    socket.send(message_coding)


def get_message(client):
    """
    Get and decode message
    :param client: Server response in binary format
    :return: Server decoding response
    """

    response = client.recv(MAX_PACKAGES)
    if isinstance(response, bytes):
        json_response = response.decode(ENCODING)
        result = json.loads(json_response)
        if isinstance(result, dict):
            return result
        raise ValueError
    raise ValueError
