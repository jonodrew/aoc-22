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
    partial_new_file = partial(make_new_file, repo)
    files = ["__init__.py", f"test_day_{day_number:02}.py", "src.py", "input.txt"]
    for file in files:
        partial_new_file(partial_path(file))


def make_new_file(repo: Repo, file_path: str) -> None:
    open(file_path, "x").close()
    repo.index.add(file_path)
