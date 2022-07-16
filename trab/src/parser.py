from .node import Node


class Parser:
    
    def __init__(self, file_path):
        self.file_path = file_path
    
    def get_node(self):

        file = open(self.file_path, 'r')
        lines = file.readlines()
        nodes_addresses = list()

        for line in lines:
        
            if "processes" in line:
                splitted = line.split()
                processes = splitted[2]

            if "id" in line:
                splitted = line.split()
                node_id = splitted[2]

            if "node" in line:
                splitted = line.split()
                nodes_addresses.append((splitted[2], splitted[3]))

        return Node(processes, node_id, nodes_addresses)