import dataclasses
import functools
from enum import IntEnum
from typing import Optional

from aoc_22.utils.read_in import read_in_from_file


class Move(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Outcome(IntEnum):
    Win = 6
    Draw = 3
    Loss = 0


def round_score(opponent_move: Move, my_move: Move) -> int:
    return my_move.value + calculate_round(my_move, opponent_move).value


def calculate_round(my_move: Move, opponent_move: Move) -> Outcome:
    if my_move == opponent_move:
        return Outcome.Draw
    elif my_move == Move.ROCK:
        return Outcome.Win if opponent_move == Move.SCISSORS else Outcome.Loss
    elif my_move == Move.SCISSORS:
        return Outcome.Win if opponent_move == Move.PAPER else Outcome.Loss
    elif my_move == Move.PAPER:
        return Outcome.Win if opponent_move == Move.ROCK else Outcome.Loss
    else:
        raise ValueError


def read_inputs():
    return [line.split(" ") for line in read_in_from_file("day_02/input.txt")]


@functools.lru_cache
def action_mapping():
    return {
        "A": Move.ROCK,
        "X": Move.ROCK,
        "B": Move.PAPER,
        "Y": Move.PAPER,
        "Z": Move.SCISSORS,
        "C": Move.SCISSORS,
    }


@functools.lru_cache
def convert_to_action(letter: str) -> Move:
    return action_mapping()[letter]


def follow_strategy():
    score = 0
    for line in read_inputs():
        score += round_score(*map(convert_to_action, line))
    return score


@dataclasses.dataclass
class Node:
    value: Move
    win: Optional["Node"] = None
    lose: Optional["Node"] = None


def outcomes_list() -> dict[Move, Node]:
    r = Node(Move.ROCK)
    p = Node(Move.PAPER)
    s = Node(Move.SCISSORS)
    s.win = r
    s.lose = p
    r.win = p
    r.lose = s
    p.win = s
    p.lose = r
    return {Move.ROCK: r, Move.PAPER: p, Move.SCISSORS: s}


def result_mapping() -> dict[str, Outcome]:
    return {"X": Outcome.Loss, "Y": Outcome.Draw, "Z": Outcome.Win}


def calculate_round_part_two(opponent_move: Move, preferred_outcome: Outcome) -> Move:
    if preferred_outcome == Outcome.Draw:
        return opponent_move
    elif preferred_outcome == Outcome.Win:
        return outcomes_list()[opponent_move].win.value
    elif preferred_outcome == Outcome.Loss:
        return outcomes_list()[opponent_move].lose.value
    else:
        raise ValueError


def score_round_part_two(opponent_move: str, preferred_option: str) -> int:
    my_move = calculate_round_part_two(
        convert_to_action(opponent_move), result_mapping()[preferred_option]
    )
    return my_move.value + result_mapping()[preferred_option].value


def follow_strategy_part_two():
    score = 0
    for line in read_inputs():
        score += score_round_part_two(*line)
    return score
