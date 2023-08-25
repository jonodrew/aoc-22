import dataclasses
from itertools import chain
from aoc_22.utils.read_in import read_in_from_file


@dataclasses.dataclass
class Tree:
    _seen: bool = False
    height: int = None

    @property
    def seen(self):
        return self._seen

    @seen.setter
    def seen(self, spotted: bool):
        self._seen = self.seen or spotted


Forest = list[list[Tree]]


def generate_forest() -> Forest:
    return [
        [Tree(False, int(h)) for h in line]
        for line in read_in_from_file("aoc_22/day_08/input.txt")
    ]


def rotate_grid(grid: Forest) -> Forest:
    return list(zip(*grid[::-1]))  # type: ignore


def count_visible(grid: Forest) -> int:
    forest_as_list = list(chain.from_iterable(grid))
    return [t.seen for t in forest_as_list].count(True)


def mark_visible_in_line(line_of_trees: list[Tree]) -> None:
    highest = -1
    for tree in line_of_trees:
        tree.seen = tree.height > highest
        highest = max(tree.height, highest)
    return None


def mark_visible_from_direction(f: Forest) -> None:
    for line in f:
        mark_visible_in_line(line)
    return None


def mark_visible_in_forest(f: Forest) -> Forest:
    mark_visible_from_direction(f)
    for i in range(3):
        f = rotate_grid(f)
        mark_visible_from_direction(f)
    return rotate_grid(f)


def beauty_score(west: int, east: int, south: int, north: int) -> int:
    return east * west * north * south


def find_trees_of_specific_height(height: int, forest: str) -> list[int]:
    return [i for i, letter in enumerate(forest) if str(height) == letter]


def part_one():
    return count_visible(mark_visible_in_forest(generate_forest()))
