from yaml import parse
from Parser.parser import Parser

def main():
    parser = Parser("Config/config_node_test.txt")
    node = parser.get_node()
    print(node)

if __name__ == "__main__":
    main()