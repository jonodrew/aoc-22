def read_in_from_file(file_path: str) -> list[str]:
    with open(file_path) as input_file:
        return [line.strip() for line in input_file.readlines()]
