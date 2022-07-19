from typing import List

from .node import Node
from .utils import Address


class Parser:
    
    def __init__(self, file_path):
        self.file_path = file_path
    
    def get_nodes(self) -> List[Node]:
        with open(self.file_path, 'r') as file:
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
