from sys import stdin

def parse(line):
    num, rest = line.split(": ", 1)
    _, n = num.split(" ")
    d = {} 
    for obj in rest.split(", "):
        k, v = obj.split(": ")
        d[k] = int(v)
    return int(n) - 1, d

sues = [None for _ in range(500)]
for line in stdin:
    n, objs = parse(line[:-1])
    sues[n] = objs

target = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

def match1(sue, target):
    return all(target[k] == v for k, v in sue.items())

def match2(sue, target):
    if "cats" in sue and sue["cats"] <= target["cats"]:
        return False
    if "trees" in sue and sue["trees"] <= target["trees"]:
        return False
    if "pomeranians" in sue and sue["pomeranians"] >= target["pomeranians"]:
        return False
    if "goldfish" in sue and sue["goldfish"] >= target["goldfish"]:
        return False
    for k in ["children", "samoyeds", "akitas", "cars", "perfumes"]:
        if k in sue and sue[k] != target[k]:
            return False
    return True

def part1(sues, target):
    for i, s in enumerate(sues):
        if match1(s, target):
            return i + 1

def part2(sues, target):
    for i, s in enumerate(sues):
        if match2(s, target):
            return i + 1

print(part1(sues, target))
print(part2(sues, target))
