from __future__ import annotations

from typing import Tuple, Dict, List

HOST: str = "127.0.0.1"
PORT: int = 5000
TOKEN: str = "token"
NUMBER_OF_PROCESS: int = 3
ADDRESS_TO_ID: Dict[Address, int] = {}


class Message:
    def __init__(self, data: str, id_: int, origin_id: int, origin_address: Address):
        self.data: str = data
        self.id: int = id_
        self.origin_id: int = origin_id
        self.origin_address: Address = origin_address

    def __eq__(self, other: Message) -> bool:
        return (self.data == other.data) and (self.id == other.id) \
               and (self.origin_id == other.origin_id)

    def to_bytes(self) -> bytes:
        return f"{self.data}#{self.id}#{self.origin_id}#{self.origin_address}".encode()


def parse_msg(data: bytes) -> Message:
    """
    Example: MsgTxt # MsgID # ProcID # ProcAddress
    """

    data = data.decode()
    splitted = data.split("#")
    msg = splitted[0]
    msg_id = splitted[1]
    proc_id = splitted[2]
    proc_address = splitted[3]

    return Message(data=msg, id_=int(msg_id),
                   origin_id=int(proc_id), origin_address=eval(proc_address))


def parser(file_path: str) -> List[List[Tuple[str, int]]]:
    with open(file_path, "r") as file:
        lines = file.readlines()
        messages: List[List[Tuple[str, int]]] = [[] for _ in range(NUMBER_OF_PROCESS)]

        for line in lines:
            splitted = line.split(":")

            origin_id: int = int(splitted[0])
            if (origin_id < 0 or origin_id >= NUMBER_OF_PROCESS):
                print(f"Erro na mensagem '{line}' \n"
                      f"ID de origem {origin_id} é inválido. \n"
                      f"Deve ser um valor entre [0, {NUMBER_OF_PROCESS - 1}]")
                exit()

            message: str = splitted[1].replace(" ", "")

            destiny_id: int = int(splitted[2])
            if (destiny_id < -1 or destiny_id >= NUMBER_OF_PROCESS):
                print(f"Erro na mensagem '{line}' \n"
                      f"ID de destino {destiny_id} é inválido. \n"
                      f"Deve ser um valor entre [-1, {NUMBER_OF_PROCESS - 1}]")
                exit()

            if (message == TOKEN and destiny_id == -1):
                print(f"Erro na mensagem '{line}' \n"
                      f"'{TOKEN}' não pode ter destino '{destiny_id}' (broadcast).")
                exit()

            messages[origin_id].append((message, destiny_id))

    return messages


def address_to_id(address: Address) -> int:
    port: int = address[1]
    port -= PORT
    return port


Address = Tuple[str, int]
Buffer = Dict[Address, List[Message]]
