from contextlib import suppress
from hashlib import sha256
from socket import socket, AF_INET, SOCK_STREAM
from typing import Tuple

BIND_ADD = ("localhost", 4321)


def socket_client(address: Tuple[str, int], server_message_length: int):
    client = socket(AF_INET, SOCK_STREAM)
    with suppress(ConnectionAbortedError):
        client.connect(address)
        while True:
            reply = client.recv(server_message_length)
            if reply == b"":
                return
            client_ack_message = sha256(reply).digest()
            client.send(client_ack_message)
