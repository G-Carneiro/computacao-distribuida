from typing import Tuple, Dict, List


class Message:
    def __init__(self, data: str, id_: int):
        self.data: str = data
        self.id: int = id_


Address = Tuple[str, int]
Buffer = Dict[Address, List[Message]]
