class Node:

    def __init__(self, processes, node_id, node_addresses):
        self.processes = processes
        self.node_id = node_id
        self.node_addresses = node_addresses

    def __str__(self):
         return f"Node\n Processes: {self.processes }\n Id: {self.node_id} \n Nodes Addresses: {self.node_addresses}"

