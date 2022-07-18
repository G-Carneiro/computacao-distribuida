from src.parser import Parser
from src.middleware import Middleware

def main():
    parser = Parser("Config/config_node_test.txt")
    node = parser.get_node()
    print(node)
    
    mid = Middleware(3)
    print(mid)

if __name__ == "__main__":
    main()
