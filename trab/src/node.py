from socket import socket, AF_INET, SOCK_STREAM
from typing import List, Dict

from .utils import Address, Buffer, Message


class Node:

    def __init__(self, address: Address, processes_address: List[Address]):
        # TODO: trocar para dicionários irá facilitar Dict[address, msg]
        self.buffer: Buffer = {address: [] for address in processes_address}
        self.input_buffer: Dict[Address, int] = {address: 0 for address in processes_address}
        self.output_buffer: Dict[Address, int] = {address: 0 for address in processes_address}
        self.received_messages: List[str] = []
        self.address: Address = address
        self.processes_address: List[Address] = processes_address
        self.client_socket = socket(AF_INET, SOCK_STREAM)

    def __str__(self):
        return (self.buffer, self.input_buffer, self.output_buffer)

    def deliver_message(self, message: str) -> None:
        self.received_messages.append(message)
        return None

    @staticmethod
    def parse_msg(data) -> Message:
        """
        Example: MsgID # MsgTxt
        """

        splitted = data.split("#")
        msg_id = splitted[0]
        msg = splitted[1]

        return Message(data=msg, id_=int(msg_id))

    def check_buffer(self, process_address: Address):
        id_msg_input = self.input_buffer[process_address]
        for msg in self.buffer[process_address]:
            if msg.id == id_msg_input:
                self.deliver_message(message=msg.data)
                self.buffer[process_address].remove(msg)    # remover do buffer tornará as buscas mais rápidas
                self.input_buffer[process_address] += 1
                self.check_buffer(process_address)
                break
            
    def on_send(self, msg, id_proc_dest):
        # não deveria ser output_buffer?
        id_msg = self.input_buffer[id_proc_dest]
        self.send_to_socket(id_proc_dest, id_msg, msg)
        self.input_buffer[id_proc_dest] += 1

    def on_recv(self, msg: bytes, process_address: Address):
        message: Message = self.parse_msg(msg)
        id_msg_input = self.input_buffer[process_address]

        if message.id == id_msg_input:
            self.deliver_message(message=message.data)
            self.input_buffer[process_address] += 1
            self.check_buffer(process_address)

        else:
            self.buffer[process_address].append(message)

    def start_socket(self):
        # pq inicializar o socket aqui? self.client_socket não era pra isso?
        with socket(AF_INET, SOCK_STREAM) as s:
            s.bind(self.address)
            s.listen()
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    self.on_recv(msg=data, process_address=addr)
                    if not data:
                        break
                    conn.sendall(data)

    def send_to_socket(self, id_proc_dest, id_msg, msg):
        # TODO: complete
        self.client_socket.connect(("127.0.0.1", 9090))
