import string
from typing import Sequence, Iterable

from aoc_22.utils.read_in import read_in_from_file


def priorities() -> dict[str, int]:
    lower = {l: i + 1 for i, l in enumerate(string.ascii_lowercase)}
    upper = {l: i + 27 for i, l in enumerate(string.ascii_uppercase)}
    return {**lower, **upper}


def find_shared(rucksack: str) -> str:
    length = len(rucksack)
    halfway = int(length / 2)
    first = rucksack[:halfway]
    second = rucksack[halfway:]
    return find_badge([first, second])


def find_badge(rucksacks: Sequence[str]) -> str:
    return set(rucksacks[0]).intersection(*(set(r) for r in rucksacks[1:])).pop()


def part_one() -> int:
    return sum(
        map(
            lambda c: priorities().get(c),
            map(find_shared, read_in_from_file("day_03/input.txt")),
        )
    )


def group_in_threes(rucksacks: Sequence[str]) -> Iterable[Sequence[str]]:
    for i, line in enumerate(rucksacks):
        if i % 3 == 0:
            yield rucksacks[i : i + 3]


def part_two() -> int:
    return sum(
        map(
            lambda c: priorities()[c],
            map(find_badge, group_in_threes(read_in_from_file("day_03/input.txt"))),
        )
    )
