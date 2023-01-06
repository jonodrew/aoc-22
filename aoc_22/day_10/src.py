from aoc_22.utils.read_in import read_in_from_file


class CPU:
    def __init__(self, registers: dict[str, int]):
        self._cycle = 0
        self.registers = registers
        self.interesting_values = set()

    def tick(self):
        self._cycle += 1
        if (self._cycle - 20) % 40 == 0:
            for r, v in self.registers.items():
                self.interesting_values.add(self._cycle*v)

    @property
    def cycle(self):
        return self._cycle

    def add(self, x: str, V: int):
        self.tick()
        self.tick()
        self.registers[x] += V

    def noop(self):
        self.tick()

    def process_instruction(self, instr: str):
        if instr == "noop":
            self.noop()
        elif instr.startswith("add"):
            self.add(instr[3].upper(), int(instr.split(" ")[-1]))
        else:
            raise ValueError


def part_one(filepath: str) -> int:
    c = CPU({"X": 1})
    for instr in read_in_from_file(filepath):
        c.process_instruction(instr)
    return sum(c.interesting_values)
