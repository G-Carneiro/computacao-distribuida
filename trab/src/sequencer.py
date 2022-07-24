from socket import socket, AF_INET, SOCK_STREAM
from typing import List

from .utils import Address, parse_msg, Message, Buffer, address_to_id


class Sequencer:
    def __init__(self, id_: int,
                 addresses: List[Address],
                 address: Address):
        self._seq_num: int = 1
        self.addresses: List[Address] = addresses
        self.address: Address = address
        self._sends_messages: Buffer = {address: [] for address in addresses}
        self._receiver_socket: socket = socket(AF_INET, SOCK_STREAM)
        self._receiver_socket.bind(address)
        self.id = id_

    def on_recv(self, msg: bytes) -> None:
        message: Message = parse_msg(msg)
        process_address = message.origin_address

        if (message in self._sends_messages[process_address]):
            print(f"{self.id}: Já havia recebido '{message.data}', ignorando...")
            return None

        print(f"{self.id}: mensagem '{message.data}', "
              f"recebida de '{message.origin_id}', aguardando para ser entregue.")

        self._sends_messages[process_address].append(message)
        broadcast_message: Message = Message(data=message.data, id_=self._seq_num,
                                             origin_id=self.id, origin_address=self.address)
        self._seq_num += 1
        self.send(message=broadcast_message, origin_address=process_address)

        return None

    def start_socket(self):
        self._receiver_socket.listen(len(self.addresses))
        while True:
            conn, addr = self._receiver_socket.accept()
            with conn:
                data = conn.recv(1024)
                self.on_recv(msg=data)
                conn.sendall(data)

    def send(self, message: Message, origin_address: Address) -> None:
        origin_address = (origin_address[0], origin_address[1] + 1)
        for address in self.addresses:
            if (origin_address != address) and (address != self.address):
                self.send_to_socket(message=message, address=address)

        return None

    def send_to_socket(self, address: Address, message: Message):
        s = socket(AF_INET, SOCK_STREAM)
        s.connect(address)
        s.sendall(message.to_bytes())
        s.close()
        print(f"{self.id}: enviou '{message.data}' para '{address_to_id(address)}'.")
        return None
