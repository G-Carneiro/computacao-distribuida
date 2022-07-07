from operator import *
from typing import Dict, Callable

from flask import Flask, request, jsonify

app = Flask(__name__)


op_to_func: Dict[str, Callable] = {
    '+': add,
    '-': sub,
    '*': mul,
    '**': pow,
    '/': truediv,
    '//': floordiv,
    '%': mod,
    '^': xor,
    '>>': rshift,
    '<<': lshift,
    'and': and_,
    '|': or_,
}


@app.route("/calculator", methods=["GET"])
def calculator():
    try:
        first_operand: int = request.args.get("first_operand", type=int)
        op: str = request.args.get("op", type=str)
        second_operand: int = request.args.get("second_operand", type=int)
        operator: Callable = op_to_func[op]
    except KeyError as error:
        raise f"{error}: Algo deu errado"
    else:
        result: float = operator(first_operand, second_operand)
        return jsonify(f"{first_operand} {op} {second_operand} = {result}")


if __name__ == "__main__":
    app.run()
