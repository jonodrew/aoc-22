import dataclasses
from utils.read_in import read_in_from_file


@dataclasses.dataclass
class CleaningArea:
    start: int
    end: int

    @property
    def range(self):
        return set(range(self.start, self.end+1))

    def contains(self, other_area: 'CleaningArea') -> bool:
        return other_area.range.issubset(self.range)

    def overlaps(self, other_area: 'CleaningArea') -> bool:
        return bool(self.range.intersection(other_area.range))


def read_in_areas() -> list[tuple[CleaningArea, CleaningArea]]:
    return [tuple(map(create_cleaning_area, line.split(",", 1))) for line in read_in_from_file("day_04/input.txt")]  # type: ignore


def create_cleaning_area(area_as_string: str) -> CleaningArea:
    area = area_as_string.split("-")
    return CleaningArea(int(area[0]), int(area[1]))


def fully_contains(area_pair: tuple[CleaningArea, CleaningArea]) -> bool:
    first_area, second_area = area_pair
    return first_area.contains(second_area) or second_area.contains(first_area)


def overlaps(area_pair: tuple[CleaningArea, CleaningArea]) -> bool:
    first_area, second_area = area_pair
    return first_area.overlaps(second_area) or second_area.overlaps(first_area)


def count_fully_contains() -> int:
    area_pairs = read_in_areas()
    return sum(map(fully_contains, area_pairs))


def count_overlaps() -> int:
    area_pairs = read_in_areas()
    return sum(map(overlaps, area_pairs))
