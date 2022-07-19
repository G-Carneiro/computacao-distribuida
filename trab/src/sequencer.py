from socket import socket, AF_INET, SOCK_STREAM
from typing import List

from .node import Node
from .utils import Address


class Sequencer:
    # TODO: será necessário um socket para realizar o envio/recebimento de mensagens
    def __init__(self, processes: List[Node], address: Address):
        self._seq_num: int = 1
        self._processes: List[Node] = processes
        self._socket: socket = socket(AF_INET, SOCK_STREAM)
        self._address: Address = address

    def receive(self, message: bytes) -> None:
        new_message: str = message.decode() + f"#{self._seq_num}"
        self._seq_num += 1
        self.send(message=bytes(new_message))
        return None

    def send(self, message: bytes) -> None:
        for process in self._processes:
            # FIXME: não vai funcionar, socket necerrário
            process.deliver_message(message.decode())

        return None
