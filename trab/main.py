from src.parser import Parser
from src.node import Node

def main():
    parser = Parser("Config/config_node_test.txt")
    node = parser.get_node()
    print(node)
    
    mid = Node(3)
    print(mid)

if __name__ == "__main__":
    main()
