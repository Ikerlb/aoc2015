from sys import stdin
from itertools import chain


funcs = {
    "hlf": lambda x: x >> 1,
    "tpl": lambda x: x * 3,
    "inc": lambda x: x + 1,
    "jie": lambda x: x % 2 == 0,
    "jio": lambda x: x == 1,
}

def parse(line):
    spl = line.split(", ")
    return spl[0].split(" ") + ([spl[1]] if len(spl) > 1 else [])

instructions = [parse(line[:-1]) for line in stdin]

# mutates regs
def execute(regs, instructions):
    pc = 0
    while pc < len(instructions):
        match instructions[pc]:
            case ["hlf" | "tpl" | "inc" as ins, reg]:
                regs[reg] = funcs[ins](regs[reg])
                pc += 1
            case ["jmp", offset]:
                pc += int(offset)
            case ["jie" | "jio" as ins, reg, offset]:
                pc += int(offset) if funcs[ins](regs[reg]) else 1
    
def part1(instructions):
    regs = {"a": 0, "b": 0}
    execute(regs, instructions)
    return regs['b']

def part2(instructions):
    regs = {"a": 1, "b": 0}
    execute(regs, instructions)
    return regs['b']

print(part1(instructions))
print(part2(instructions))
