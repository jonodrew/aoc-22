def next_set(previous_set: set, new_char: str) -> set:
    return previous_set.union(set(new_char))


def check_window(w: set) -> bool:
    return len(w) == 4


def process_string(input_str: str) -> int:
    start = 0
    end = 4
    window = set(input_str[start:end])
    while not check_window(window):
        end += 1
        start += 1
        window = set(input_str[start:end])
    return end
