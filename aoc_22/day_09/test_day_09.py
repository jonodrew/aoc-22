import pytest
from .src import greater_than_length, Position, tail_step


@pytest.mark.parametrize(
    ["head_pos", "tail_pos", "longer"],
    [[(2, 1), (0, 1), True], [(2, 1), (1, 1), False], [(-1, 0), (1, 0), True]],
)
def test_greater_than_length(head_pos, tail_pos, longer):
    assert greater_than_length(Position(*head_pos), Position(*tail_pos)) == longer


@pytest.mark.parametrize(
    ["diff", "expected_position"],
    [[(2, 0), (1, 0)], [(-2, 0), (-1, 0)], [(0, 2), (0, 1)], [(0, -2), (0, -1)]],
)
def test_cardinal_move(diff, expected_position):
    diff = Position(*diff)
    tail = Position(0, 0)
    assert tail.cardinal_move(diff) == Position(*expected_position)


@pytest.mark.parametrize(
    ["head", "tail", "expected_tail"],
    [
        (Position(2, 0), Position(0, 0), Position(1, 0)),
        (Position(4, 2), Position(4, 0), Position(4, 1)),
        (Position(-5, 3), Position(-3, 3), Position(-4, 3)),
        (Position(3, 4), Position(2, 2), Position(3, 3)),
        (Position(1, 1), Position(0, 0), Position(0, 0)),
    ],
)
def test_tail_move(head, tail, expected_tail):
    assert tail_step(tail, head) == expected_tail
