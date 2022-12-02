from typing import Sequence

from utils.read_in import read_in_from_file


def read_elf_calories(inputs: Sequence[str]) -> set[int]:
    lines = inputs
    elves = set()
    calories = 0
    for line in lines:
        if line != "\n":
            calories += int(line)
        else:
            elves.add(calories)
            calories = 0
    return elves


def part_one() -> int:
    return max(read_elf_calories(read_in_from_file("input.txt")))


def part_two() -> int:
    elves = read_elf_calories(read_in_from_file("input.txt"))
    most_calories = sorted(elves, reverse=True)
    return sum(most_calories[:3])


def main():
    print(part_one())
    print(part_two())


main()
