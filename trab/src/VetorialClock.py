from __future__ import annotations

from operator import gt, ne, lt
from typing import List, Callable


class VetorialClock:
    def __init__(self, process_number: int) -> None:
        self._process_number: int = process_number
        self._vector: List[int] = [0] * process_number

    def vector(self) -> List[int]:
        return self._vector

    def process_number(self) -> int:
        return self._process_number

    def before_send(self, process_id: int) -> None:
        self._vector[process_id] += 1
        return None

    def after_receive(self, process_id: int, other: VetorialClock) -> None:
        for i in range(self._process_number):
            self._vector[i] += 1
            if (i != process_id):
                self._vector[i] = max(self._vector[i], other[i])

        return None

    def _compare(self, other: VetorialClock, operator: Callable, cond_return: bool = False) -> bool:
        for i in range(self._process_number):
            if operator(self._vector[i], other[i]):
                return cond_return

        return not cond_return

    def __eq__(self, other: VetorialClock) -> bool:
        return self._compare(other=other, operator=ne)

    def __le__(self, other: VetorialClock) -> bool:
        return self._compare(other=other, operator=gt)

    def __lt__(self, other: VetorialClock) -> bool:
        return (self <= other) and self._compare(other=other, operator=lt, cond_return=True)

    def __getitem__(self, item: int) -> int:
        return self._vector[item]

    def concurrent(self, other: VetorialClock) -> bool:
        return (not (self <= other) and not (other <= self))

    def causal(self, other: VetorialClock) -> bool:
        return (self < other)
