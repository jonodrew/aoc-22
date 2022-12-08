import pytest
from .src import count_visible, Tree, mark_visible_in_forest


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
