from functools import partial
import click
import os
from git import Repo


@click.command
@click.argument("day_number", type=int)
def create_new_day(day_number):
    dir_path = f"aoc_22/day_{day_number:02}"
    os.makedirs(dir_path)
    partial_path = partial(os.path.join, dir_path)
    repo = Repo(".")
    make_new_file(partial_path("__init__.py"), repo)
    make_new_file(partial_path(f"test_day_{day_number:02}.py"), repo)
    make_new_file(partial_path("src.py"), repo)
    make_new_file(partial_path("input.txt"), repo)


def make_new_file(file_path: str, repo: Repo) -> None:
    open(file_path, "x").close()
    repo.index.add(file_path)
