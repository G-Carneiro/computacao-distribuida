from typing import List

from src.node import Node
from src.parser import Parser


def main():
    parser = Parser("Config/config_node_test.txt")
    nodes: List[Node] = parser.get_nodes()
    print(nodes)
    

if __name__ == "__main__":
    main()
