from day_02.src import follow_strategy
from unittest.mock import patch


def test_follow_strategy():
    with patch("day_02.src.read_inputs", return_value=[["A", "Y"], ["B", "X"], ["C", "Z"]]) as inputs:
        assert follow_strategy() == 15
