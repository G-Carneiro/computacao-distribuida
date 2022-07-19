from typing import Tuple, Dict, List

from .node import Node


class Message:
    def __init__(self, data: str, id_: int):
        self.data: str = data
        self.id: int = id_


Address = Tuple[str, int]
Buffer = Dict[Address, List[Message]]


def parser(file_path: str) -> List[Node]:
    with open(file_path, 'r') as file:
        lines = file.readlines()
        nodes_addresses: List[Address] = list()

        for line in lines:
            splitted = line.split(":")
            host: str = splitted[0]
            port: int = int(splitted[1])
            address: Address = (host, port)
            nodes_addresses.append(address)

    nodes: List[Node] = []
    for address in nodes_addresses:
        new_node: Node = Node(address=address, processes_address=nodes_addresses)
        nodes.append(new_node)

    return nodes
