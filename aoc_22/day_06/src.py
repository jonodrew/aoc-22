def next_set(previous_set: set, new_char: str) -> set:
    return previous_set.union(set(new_char))


def check_window(w: set, unique_chars: int) -> bool:
    return len(w) == unique_chars


def process_string(input_str: str, unique_characters: int) -> int:
    start = 0
    end = unique_characters
    window = set(input_str[start:end])
    while not check_window(window, unique_characters):
        end += 1
        start += 1
        window_str = input_str[start:end]
        window = set(window_str)
    return end
