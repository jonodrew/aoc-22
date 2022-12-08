from unittest.mock import patch

from .src import part_one, read_in_from_file


@patch(
    "aoc_22.day_07.src.read_in_from_file",
    return_value=read_in_from_file("aoc_22/day_07/test_input.txt"),
)
def test_part_one(patched_inputs):
    assert part_one() == 95437
