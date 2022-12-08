import re
from typing import Optional, Sequence, Callable
from aoc_22.utils.read_in import read_in_from_file

TOTAL_FILE_SIZE = 70000000
SPACE_REQUIRED = 30000000


class FileNode:
    def __init__(self, name: str, parent: Optional["FileNode"] = None):
        self.children: dict[str, Optional["FileNode"]] = {}
        self.name = name
        self._size: int = 0
        self.parent: Optional["FileNode"] = parent

    @property
    def size(self):
        return self._size

    def add_file_size(self, file_size: int) -> None:
        if self.parent is not None:
            self.parent.add_file_size(file_size)
        self._size += file_size


def change_dir(cmd_args: str, file_tree: FileNode):
    if cmd_args == "/":
        return return_to_root(file_tree)
    elif cmd_args == "..":
        return file_tree.parent
    else:
        return file_tree.children[cmd_args]


def return_to_root(node: FileNode) -> FileNode:
    while node.parent is not None:
        return return_to_root(node.parent)
    return node


def parse_input(cmd_line: str, file_tree: FileNode) -> FileNode:
    args = cmd_line.split(" ")
    determiner = args[0]
    if determiner == "$" and args[1] != "ls":
        file_tree = change_dir(args[2], file_tree)
    elif determiner == "dir":
        file_tree.children[args[1]] = FileNode(name=args[1], parent=file_tree)
    elif re.compile(r"^\d+").search(determiner):
        addition = int(determiner)
        file_tree.add_file_size(addition)
    return file_tree


def parse_command_line(command_line_output: Sequence[str]) -> FileNode:
    current_folder = FileNode(name="/", parent=None)
    for line in command_line_output[1:]:
        current_folder = parse_input(line, current_folder)
    return current_folder


def flatten_tree(root: FileNode) -> list[FileNode]:
    r = [root]
    for child in root.children.values():
        r.extend(flatten_tree(child))
    return r


def find_all_dirs_with(
    comparison_func: Callable[[FileNode], bool], root_node: FileNode
) -> set[FileNode]:
    return set(filter(comparison_func, flatten_tree(root_node)))


def tree_from_file() -> FileNode:
    return parse_command_line(read_in_from_file("aoc_22/day_07/input.txt"))


def part_one():
    tree = return_to_root(tree_from_file())
    return sum(
        map(lambda f: f.size, find_all_dirs_with(lambda f: f.size < 100000, tree))
    )


def unused_space(root_node: FileNode) -> int:
    return TOTAL_FILE_SIZE - root_node.size


def min_size_to_delete(root_node: FileNode) -> int:
    return SPACE_REQUIRED - unused_space(root_node)


def part_two():
    root = return_to_root(tree_from_file())
    return sorted(
        map(
            lambda f: f.size,
            find_all_dirs_with(lambda f: f.size >= min_size_to_delete(root), root),
        )
    )[0]
