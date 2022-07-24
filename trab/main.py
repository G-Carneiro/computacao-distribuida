from multiprocessing import Process
from typing import List, Dict, Tuple

from src.node import Node
from src.sequencer import Sequencer
from src.utils import Address, HOST, PORT, NUMBER_OF_PROCESS


def receiver(node: Node) -> None:
    node.start_socket()
    return None


def sender(node: Node) -> None:
    # if node.address == ('127.0.0.1', 5000):
        # node.send_to_socket(('127.0.0.1', 5003), "oi")
        # node.send_to_socket((HOST, 5002), "hi")
        # node.send_to_socket((HOST, 5002), "hi2")
    # if node.address == ('127.0.0.1', 5005):
    #     node.send_to_socket(('127.0.0.1', 5003), "oi")
    #     node.send_to_socket((HOST, 5003), "hi")
    return None


def token_ring(nodes: List[Node]) -> None:
    nodes[0].send_to_socket(nodes[1].address, data="token")
    return None


def main():
    nodes: List[Node] = []
    addresses: List[Address] = []
    for i in range(NUMBER_OF_PROCESS + 1):
        new_sender: Address = (HOST, PORT + i)
        addresses.append(new_sender)

    sequencer: Sequencer = Sequencer(id_=NUMBER_OF_PROCESS, addresses=addresses,
                                     address=addresses[-1])
    for i in range(NUMBER_OF_PROCESS):
        new_node: Node = Node(id_=i, address=addresses[i], addresses=addresses,
                              sequencer_address=sequencer.address)
        nodes.append(new_node)
    processes: Dict[Node, Tuple[Process, Process]] = {}
    sequencer_sender = Process(name="Sequencer sender", target=sender, args=(sequencer,))
    sequencer_receiver = Process(name="Sequencer receiver", target=receiver, args=(sequencer,))
    sequencer_receiver.start()
    sequencer_sender.start()
    for node in nodes:
        new_sender: Process = Process(name=f"{node.id} - Sender", target=sender, args=(node,))
        new_receiver: Process = Process(name=f"{node.id} - Receiver", target=receiver, args=(node,))
        new_receiver.start()
        processes[node] = (new_sender, new_receiver)

    for node in processes:
        processes[node][0].start()

    token_ring(nodes=nodes)

    for proc1, proc2 in processes.values():
        proc1.join()
        proc2.join()

    sequencer_sender.join()
    sequencer_receiver.join()


if __name__ == "__main__":
    main()
