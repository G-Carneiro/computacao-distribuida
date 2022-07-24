from multiprocessing import Process
from typing import List, Dict, Tuple

from src.node import Node
from src.sequencer import Sequencer
from src.utils import Address, HOST, PORT, NUMBER_OF_PROCESS


def receiver(node: Node) -> None:
    node.start_socket()
    return None


def sender(node: Node) -> None:
    if node.receiver_address == ('127.0.0.1', 5001):
        node.send_to_socket(('127.0.0.1', 5003), "oi")
        node.send_to_socket((HOST, 5003), "hi")
    if node.receiver_address == ('127.0.0.1', 5005):
        node.send_to_socket(('127.0.0.1', 5003), "oi")
        node.send_to_socket((HOST, 5003), "hi")
    return None


def main():
    nodes: List[Node] = []
    senders_addresses: List[Address] = []
    receivers_addresses: List[Address] = []
    for i in range(0, 2 * NUMBER_OF_PROCESS + 1, 2):
        new_sender: Address = (HOST, PORT + i)
        new_receiver: Address = (HOST, PORT + i + 1)
        senders_addresses.append(new_sender)
        receivers_addresses.append(new_receiver)

    for i in range(NUMBER_OF_PROCESS):
        new_node: Node = Node(id_=i,
                              sender_address=senders_addresses[i],
                              receiver_address=receivers_addresses[i],
                              senders_addresses=senders_addresses,
                              receivers_addresses=receivers_addresses)
        nodes.append(new_node)
    processes: Dict[Node, Tuple[Process, Process]] = {}
    sequencer: Sequencer = Sequencer(id_=NUMBER_OF_PROCESS,
                                     senders_addresses=senders_addresses,
                                     receivers_addresses=receivers_addresses,
                                     sender_address=senders_addresses[-1],
                                     receiver_address=receivers_addresses[-1])
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

    for proc1, proc2 in processes.values():
        proc1.join()
        proc2.join()

    sequencer_sender.join()
    sequencer_receiver.join()


if __name__ == "__main__":
    main()
