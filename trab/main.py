from multiprocessing import Process
from time import sleep
from typing import List, Tuple, Union, Dict

from src.node import Node
from src.sequencer import Sequencer
from src.utils import Address, HOST, PORT, NUMBER_OF_PROCESS, parser, Message

nodes: List[Union[Node, Sequencer]] = []


def receiver(node: Node) -> None:
    node.start_socket()
    return None


def sender(node: Node, messages: Tuple[str, int]) -> None:
    for message, destiny_id in messages:
        node.send_to_socket(address=nodes[destiny_id].address, data=message)

    return None


def token_ring(nodes: List[Node]) -> None:
    nodes[0].send_to_socket(nodes[1].address, data="token")
    return None


def broadcast() -> None:
    pass


def main() -> None:
    messages: Dict[int, List[Tuple[str, int]]] = parser("Config/config_node_test.txt")
    addresses: List[Address] = []

    # inicializa todos endereços
    for i in range(NUMBER_OF_PROCESS + 1):
        new_address: Address = (HOST, PORT + i)
        addresses.append(new_address)

    # cria o sequencer (usado para mensagens broadcast)
    sequencer_address: Address = addresses[-1]
    sequencer: Sequencer = Sequencer(id_=NUMBER_OF_PROCESS, addresses=addresses,
                                     address=sequencer_address)
    sequencer_receiver = Process(name="Processo Sequencer", target=receiver, args=(sequencer,))
    sequencer_receiver.start()

    # cria os nodos e processos para recebimento de mensagens
    receivers_processes: List[Process] = []
    for i in range(NUMBER_OF_PROCESS):
        node: Node = Node(id_=i, address=addresses[i], addresses=addresses)
        nodes.append(node)

        new_receiver: Process = Process(name=f"Processo {node.id} - Receiver", target=receiver, args=(node,))
        receivers_processes.append(new_receiver)
        new_receiver.start()

    # adiciona o sequencer a lista de nós conhecidos
    nodes.append(sequencer)

    # token_ring(nodes=nodes)

    # cria processos para envio de cada mensagem
    senders_processes: List[Process] = []
    for i in range(NUMBER_OF_PROCESS):
        new_sender: Process = Process(name=f"Processo {i} - Sender",
                                      target=sender, args=(nodes[i], messages[i]))
        senders_processes.append(new_sender)
        new_sender.start()

    # espera até que todos senders terminem, ou seja,
    # que todas as mensagens sejam enviadas
    for process in senders_processes:
        process.join()

    # para evitar problemas de encerrar receivers antes de
    # receberem todas as mensagens um sleep será usado
    # como os receivers ‘sockets’ estão sempre em ‘loop’ é necessário
    # forçar sua para parada com um terminate(), caso isso seka feito
    # antes do recebimento e tratamento da mensagem, pode gerar problemas
    # isso também afetará o algoritmo de ‘token ring’, visto que ele fica
    # mandando mensagens pela rede em ‘loop’
    # esse número pode ser aumentado caso não seja suficiente para rodar
    # os arquivos de teste
    sleep(30)

    # após todas as mensagens serem enviadas, os receivers
    # também podem finalizar
    for process in receivers_processes:
        print(f"Finalizando '{process.name}'")
        process.terminate()

    # por fim, o sequencer também pode encerrar
    print(f"Finalizando '{sequencer_receiver.name}'")
    sequencer_receiver.terminate()

    print("Todas as mensagens foram enviadas.")

    return None


if __name__ == "__main__":
    main()
