from unittest.mock import patch
from .src import compute_instruction, Instruction, final_position


def inputs():
    return """move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2""".split(
        "\n"
    )


def test_compute_instruction():
    assert compute_instruction("move 2 from 4 to 2") == Instruction(2, 4, 2)


@patch("aoc_22.day_05.src.starting_stacks", return_value=["NZ", "DCM", "P"])
@patch("aoc_22.day_05.src.read_in_from_file", return_value=inputs())
def test_final_position(inputs, stacks):
    assert final_position() == "CMZ"


@patch("aoc_22.day_05.src.starting_stacks", return_value=["NZ", "DCM", "P"])
@patch("aoc_22.day_05.src.read_in_from_file", return_value=inputs())
def test_final_position_with_9001(inputs, stacks):
    assert final_position(9001) == "MCD"
