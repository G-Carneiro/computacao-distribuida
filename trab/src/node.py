from socket import socket, AF_INET, SOCK_STREAM
from typing import List, Dict

from .utils import Address, Buffer, Message, parse_msg, address_to_id


class Node:

    def __init__(self, id_: int,
                 receiver_address: Address,
                 sender_address: Address,
                 receivers_addresses: List[Address],
                 senders_addresses: List[Address]):
        self.buffer: Buffer = {address: [] for address in senders_addresses}
        self.input_buffer: Dict[Address, int] = {address: 0 for address in senders_addresses}
        self.output_buffer: Dict[Address, int] = {address: 0 for address in receivers_addresses}
        self.received_messages: List[Message] = []
        self.receiver_address: Address = receiver_address
        self.sender_address: Address = sender_address
        self.senders_addresses: List[Address] = senders_addresses
        self.receivers_addresses: List[Address] = receivers_addresses
        self.receiver_socket = socket(AF_INET, SOCK_STREAM)
        self.receiver_socket.bind(self.receiver_address)
        self.id = id_

    def __str__(self):
        return (self.buffer, self.input_buffer, self.output_buffer)

    def __repr__(self):
        return f"{self.receiver_address}"

    def deliver_message(self, message: Message) -> None:
        self.received_messages.append(message)
        return None

    def check_buffer(self, process_address: Address):
        id_msg_input = self.input_buffer[process_address]
        for msg in self.buffer[process_address]:
            if msg.id == id_msg_input:
                self.deliver_message(message=msg)
                self.buffer[process_address].remove(msg)    # remover do buffer tornará as buscas mais rápidas
                self.input_buffer[process_address] += 1
                self.check_buffer(process_address)
                break
            
    def on_send(self, message: str, destiny_address: Address) -> bytes:
        id_msg = self.output_buffer[destiny_address]
        message += f"#{id_msg}#{self.id}#{self.sender_address}"
        self.output_buffer[destiny_address] += 1
        return message.encode()

    def on_recv(self, msg: bytes) -> None:
        message: Message = parse_msg(msg)
        process_address = message.origin_address
        try:
            process_buffer = self.buffer[process_address]
        except KeyError:
            print(f"Erro: endereço {process_address} não reconhecido.")
            return None

        if (message in process_buffer + self.received_messages):
            return None
        id_msg_input = self.input_buffer[process_address]

        if message.id == id_msg_input:
            self.deliver_message(message=message)
            self.input_buffer[process_address] += 1
            self.check_buffer(process_address)

        else:
            self.buffer[process_address].append(message)

        print(f"{self.id} received '{message.data}' "
              f"from {message.origin_id}.")

        return None

    def start_socket(self):
        self.receiver_socket.listen(len(self.senders_addresses))
        while True:
            conn, addr = self.receiver_socket.accept()
            with conn:
                data = conn.recv(1024)
                self.on_recv(msg=data)
                conn.sendall(data)

    def send_to_socket(self, address: Address, data: str) -> None:
        message: bytes = self.on_send(message=data, destiny_address=address)
        s = socket(AF_INET, SOCK_STREAM)
        s.connect(address)
        s.sendall(message)
        s.close()
        print(f"{self.id} send '{data}' to {address_to_id(address)}{address}.")
        return None
