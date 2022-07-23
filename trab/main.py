from typing import List, Dict, Tuple
from multiprocessing import Process

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


def receiver(node: Node) -> None:
    node.start_socket()
    return None


def sender(node: Node) -> None:
    if node.address == ("localhost", 4000):
        node.send_to_socket(("localhost", 5000), "oi")
    return None


def main():
    nodes: List[Node] = parser("Config/config_node_test.txt")
    print(nodes)
    processes: Dict[Node, Tuple[Process, Process]] = {}

    for node in nodes:
        new_sender: Process = Process(target=sender, args=(node,))
        new_receiver: Process = Process(target=receiver, args=(node,))
        new_receiver.start()
        new_sender.start()
        processes[node] = (new_sender, new_receiver)


if __name__ == "__main__":
    main()
