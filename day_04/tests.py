from unittest.mock import patch
from day_04.src import count_overlaps


def inputs_for_test():
    input_string = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
    return input_string.split("\n")


def test_count_overlaps():
    with patch("day_04.src.read_in_from_file", return_value=inputs_for_test()):
        assert count_overlaps() == 4
