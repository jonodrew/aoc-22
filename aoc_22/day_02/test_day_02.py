from aoc_22.day_02.src import follow_strategy, follow_strategy_part_two
from unittest.mock import patch


def test_follow_strategy():
    with patch(
        "aoc_22.day_02.src.read_inputs",
        return_value=[["A", "Y"], ["B", "X"], ["C", "Z"]],
    ):
        assert follow_strategy() == 15


def test_part_two_strategy():
    with patch(
        "aoc_22.day_02.src.read_inputs",
        return_value=[["A", "Y"], ["B", "X"], ["C", "Z"]],
    ):
        assert follow_strategy_part_two() == 12
