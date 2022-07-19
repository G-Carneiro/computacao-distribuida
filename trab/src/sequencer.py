from typing import List

from .node import Node


class Sequencer:
    # TODO: será necessário um socket para realizar o envio/recebimento de mensagens
    def __init__(self, processes: List[Node]):
        self._seq_num: int = 1
        self._processes: List[Node] = processes

    def receive(self, message: bytes) -> None:
        new_message: str = message.decode() + f"#{self._seq_num}"
        self._seq_num += 1
        self.send(message=bytes(new_message))
        return None

    def send(self, message: bytes) -> None:
        for process in self._processes:
            process.deliver_message(message)

        return None
