from __future__ import annotations

from collections import namedtuple
from typing import Literal
from typing import Type

from aoc_22.utils.read_in import read_in_from_file

CrateStack = list[str]

Instruction = namedtuple("Instruction", ["quantity", "from_stack", "to_stack"])


class Crane:
    def __init__(self, crate_stacks: dict[int, CrateStack]):
        self.crate_stacks = crate_stacks

    def move(self, i: Instruction):
        crates = self._pickup(i.quantity, i.from_stack)
        self.crate_stacks[i.to_stack].extend(crates)

    def _pickup(self, quantity: int, from_stack: int) -> CrateStack:
        return [self.crate_stacks[from_stack].pop() for _ in range(quantity)]


class Model9001(Crane):
    def _pickup(self, quantity: int, from_stack: int) -> CrateStack:
        crates = super()._pickup(quantity, from_stack)
        crates.reverse()
        return crates


def compute_instruction(instruction: str) -> Instruction:
    instructions = instruction.split(" ")
    return Instruction(*map(int, (instructions[1], instructions[3], instructions[5])))


def split_string(crates: str) -> CrateStack:
    crates_as_list = [c for c in crates]
    crates_as_list.reverse()
    return crates_as_list


def starting_position(model: type[Crane] = Crane) -> Crane:
    return model(
        {i + 1: split_string(crates) for i, crates in enumerate(starting_stacks())}
    )


def starting_stacks() -> list[str]:
    return [
        "CSGB",
        "GVNJHWMT",
        "SQM",
        "MNWTLSB",
        "PWGVTFZJ",
        "SHQGBTC",
        "WBPJT",
        "MQTFZCDG",
        "FPBHSN",
    ]


Model = Literal[9000, 9001]


def final_position(m: Model = 9000) -> str:
    models: dict[Model, Type[Crane]] = {9000: Crane, 9001: Model9001}
    crane = starting_position(models[m])
    for instruction in map(
        compute_instruction, read_in_from_file("aoc_22/day_05/input.txt")
    ):
        crane.move(instruction)
    return "".join(stack[-1] for stack in crane.crate_stacks.values())
