from unittest.mock import patch

import pytest

from day_04.src import count_overlaps, count_fully_contains


def inputs_for_test():
    input_string = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
    return input_string.split("\n")


@pytest.fixture(autouse=True)
def patch_inputs():
    with patch("day_04.src.read_in_from_file", return_value=inputs_for_test()):
        yield


def test_count_overlaps(patch_inputs):
    assert count_overlaps() == 4


def test_count_contains(patch_inputs):
    assert count_fully_contains() == 2
