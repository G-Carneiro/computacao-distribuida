class Node:

    def __init__(self, processes, node_id, node_addresses):
        self.processes = processes
        self.node_id = node_id
        self.node_addresses = node_addresses

    def __str__(self):
        return f"Node \n" \
               f"Processes: {self.processes } \n" \
               f"Id: {self.node_id} \n" \
               f"Nodes Addresses: {self.node_addresses}"

