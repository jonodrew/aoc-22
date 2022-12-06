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
    assert process_string(test_input) == position
