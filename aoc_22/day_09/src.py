import dataclasses
import functools
from typing import Literal, Iterator
from aoc_22.utils.read_in import read_in_from_file


@dataclasses.dataclass(frozen=True)
class Position:
    x: int = 0
    y: int = 0

    def difference(self, other: "Position") -> "Position":
        return Position(other.x - self.x, other.y - self.y)

    def on_top(self, other: "Position") -> bool:
        return self.difference(other) == Position(0, 0)

    def cardinal_move(self, diff: "Position"):
        """

        :param diff: th
        :return:
        """
        return Position(self.x + diff.x // 2, self.y + diff.y // 2)

    def diagonal_move(self, diff: "Position"):
        if diff.x in (-1, 1):
            half_step = Position(self.x + diff.x, self.y)
        elif diff.y in (-1, 1):
            half_step = Position(self.x, self.y + diff.y)
        else:
            raise ValueError
        return half_step

    @property
    def coords(self):
        return self.x, self.y


Direction = Literal["U", "D", "L", "R"]
Instruction = tuple[Direction, int]


def planck_length() -> int:
    return 1


@functools.lru_cache
def step(d: Direction) -> Position:
    return {
        "U": Position(0, 1),
        "D": Position(0, -1),
        "L": Position(-1, 0),
        "R": Position(1, 0),
    }[d]


def read_instructions(filepath: str) -> Iterator[Instruction]:
    for instr in read_in_from_file(filepath):
        direction, value = tuple(instr.split(" "))
        if direction in {"U", "D", "L", "R"}:
            yield direction, int(value)  # type: ignore


def process_instruction(i: Instruction) -> list[Position]:
    dir, distance = i
    return [step(dir) for _ in range(distance)]


def compute_instruction(
    h: Position, t: Position, instr: Instruction
) -> tuple[Position, Position, set[Position]]:
    tail_positions = set()
    for p in process_instruction(instr):
        h = head_move(h, p)
        t = tail_step(t, h)
        tail_positions.add(t)
    return h, t, tail_positions


def calculate_final() -> set[Position]:
    head = Position(0, 0)
    tail = Position(0, 0)
    tail_positions = set()
    tail_positions.add(tail)
    for i in read_instructions("aoc_22/day_09/input.txt"):
        head, tail, positions = compute_instruction(head, tail, i)
        tail_positions = tail_positions.union(positions)
    return tail_positions


def head_move(current: Position, move: Position) -> Position:
    return Position(current.x + move.x, current.y + move.y)


def tail_step(tail: Position, head: Position) -> Position:
    if greater_than_length(tail, head):
        # step towards the head by the shortest method, ie such that the absolute delta becomes at most (1, 1)
        diff = tail.difference(head)
        if any(map(lambda p: p == 0, diff.coords)):
            return tail.cardinal_move(diff)
        else:
            half_step = tail.diagonal_move(diff)
            return tail_step(half_step, head)
    return tail


def greater_than_length(tail: Position, head: Position) -> bool:
    return any(
        map(
            lambda attr: abs(getattr(head, attr) - getattr(tail, attr))
            > planck_length(),
            ("y", "x"),
        )
    )
