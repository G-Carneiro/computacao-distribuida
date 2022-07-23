from typing import List, Dict, Tuple
from multiprocessing import Process

from src.node import Node
from src.utils import Address


def parser(file_path: str) -> List[Node]:
    with open(file_path, 'r') as file:
        lines = file.readlines()
        receiver_addresses: List[Address] = []
        sender_addresses: List[Address] = []
        host: str = '127.0.0.1'

        for line in lines:
            splitted = line.split()
            sender_port: int = int(splitted[0])
            receiver_port: int = int(splitted[1])
            receiver_address: Address = (host, receiver_port)
            sender_address: Address = (host, sender_port)
            receiver_addresses.append(receiver_address)
            sender_addresses.append(sender_address)

    nodes: List[Node] = []
    for i in range(len(receiver_addresses)):
        new_node: Node = Node(receiver_address=receiver_addresses[i],
                              sender_address=sender_addresses[i],
                              receivers_addresses=receiver_addresses,
                              senders_addresses=sender_addresses)
        nodes.append(new_node)

    return nodes


def receiver(node: Node) -> None:
    node.start_socket()
    return None


def sender(node: Node) -> None:
    if node.receiver_address == ('127.0.0.1', 4001):
        node.send_to_socket(('127.0.0.1', 5001), "oi")
    return None


def main():
    nodes: List[Node] = parser("Config/config_node_test.txt")
    print(nodes)
    processes: Dict[Node, Tuple[Process, Process]] = {}

    for node in nodes:
        new_sender: Process = Process(name=f"{node.receiver_address} - Sender", target=sender, args=(node,))
        new_receiver: Process = Process(name=f"{node.receiver_address} - Receiver", target=receiver, args=(node,))
        new_receiver.start()
        new_sender.start()
        processes[node] = (new_sender, new_receiver)


if __name__ == "__main__":
    main()
