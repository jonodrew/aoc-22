import dataclasses
import functools
from typing import Iterator

from utils.read_in import read_in_from_file


@dataclasses.dataclass
class CleaningArea:
    start: int
    end: int

    @functools.cached_property
    def range(self):
        return set(range(self.start, self.end + 1))

    def contains(self, other_area: "CleaningArea") -> bool:
        return other_area.range.issubset(self.range)

    def overlaps(self, other_area: "CleaningArea") -> bool:
        return bool(self.range.intersection(other_area.range))


AreaPair = tuple[CleaningArea, CleaningArea]


def read_in_areas() -> Iterator[AreaPair]:
    return map(create_cleaning_area_pair, read_in_from_file("day_04/input.txt"))


def create_cleaning_area_pair(paired_areas: str) -> AreaPair:
    areas = paired_areas.split(",")
    return create_cleaning_area(areas[0]), create_cleaning_area(areas[1])


def create_cleaning_area(area_as_string: str) -> CleaningArea:
    area = area_as_string.split("-")
    return CleaningArea(int(area[0]), int(area[1]))


def fully_contains(area_pair: AreaPair) -> bool:
    first_area, second_area = area_pair
    return first_area.contains(second_area) or second_area.contains(first_area)


def overlaps(area_pair: AreaPair) -> bool:
    first_area, second_area = area_pair
    return first_area.overlaps(second_area) or second_area.overlaps(first_area)


def count_fully_contains() -> int:
    area_pairs = read_in_areas()
    return sum(map(fully_contains, area_pairs))


def count_overlaps() -> int:
    area_pairs = read_in_areas()
    return sum(map(overlaps, area_pairs))
