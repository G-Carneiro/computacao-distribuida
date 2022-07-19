from typing import List

from src.node import Node
from src.utils import parser


def main():
    nodes: List[Node] = parser("Config/config_node_test.txt")
    print(nodes)
    

if __name__ == "__main__":
    main()
