from json import dumps

from requests import get

while True:
    try:
        entry: str = input("Digite a conta que deseja resolver (CTRL + C to exit): ")
        first_operand, op, second_operand = entry.split(" ")
    except KeyboardInterrupt:
        print()
        exit(0)
    else:
        url: str = f"http://localhost:5000/calculator?first_operand={first_operand}&op={op}" \
                   f"&second_operand={second_operand}"
        result = get(url)
        print(dumps(result.json()))
