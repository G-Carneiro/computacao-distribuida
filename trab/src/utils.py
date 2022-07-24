from __future__ import annotations

from typing import Tuple, Dict, List

HOST: str = "127.0.0.1"
PORT: int = 5000
NUMBER_OF_PROCESS: int = 3
ADDRESS_TO_ID: Dict[Address, int] = {}


class Message:
    def __init__(self, data: str, id_: int, origin_id: int, origin_address: Address):
        self.data: str = data
        self.id: int = id_
        self.origin_id: int = origin_id
        self.origin_address: Address = origin_address

    def __eq__(self, other: Message) -> bool:
        return (self.data == other.data) and (self.id == other.id)

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


def address_to_id(address: Address) -> int:
    port: int = address[1]
    port -= PORT
    if (port % 2):
        port -= 1
    port //= 2
    return port


Address = Tuple[str, int]
Buffer = Dict[Address, List[Message]]
