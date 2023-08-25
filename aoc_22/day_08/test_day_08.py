import pytest
from .src import (
    count_visible,
    Tree,
    mark_visible_in_forest,
    beauty_score,
    find_trees_of_specific_height,
)


@pytest.fixture
def test_forest_string() -> str:
    return """30373
25512
65332
33549
35390"""


@pytest.fixture(autouse=True)
def test_inputs():
    return [
        line
        for line in """30373
25512
65332
33549
35390""".split(
            "\n"
        )
    ]


def test_count_visible(test_inputs):
    assert (
        count_visible(
            mark_visible_in_forest(
                [[Tree(False, int(h)) for h in line] for line in test_inputs]
            )
        )
        == 21
    )


@pytest.mark.parametrize(
    ["south", "west", "east", "north", "expected"], [(0, 0, 0, 0, 0), (1, 1, 1, 1, 1)]
)
def test_beauty_score(south, west, east, north, expected):
    assert beauty_score(south, east, west, north) == expected


@pytest.mark.parametrize(["height", "location"], [(7, [3]), (0, [1, 28])])
def test_find_trees(test_forest_string, height, location):
    assert find_trees_of_specific_height(height, test_forest_string) == location
