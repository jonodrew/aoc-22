import pytest

from .src import process_string


@pytest.mark.parametrize(
    ["test_input", "position"],
    [
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
        ("nppdvjthqldpwncqszvftbrmjlhg", 6),
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
    ],
)
def test_process_string(test_input, position):
    assert process_string(test_input, 4) == position


@pytest.mark.parametrize(
    ["test_input", "position"],
    [
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
        ("nppdvjthqldpwncqszvftbrmjlhg", 23),
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
    ],
)
def test_message_marker(test_input, position):
    assert process_string(test_input, 14) == position
