from typing import List

from src.node import Node
from src.utils import Address


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


def main():
    nodes: List[Node] = parser("Config/config_node_test.txt")
    print(nodes)
    

if __name__ == "__main__":
    main()
