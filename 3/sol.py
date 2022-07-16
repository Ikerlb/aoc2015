from collections import defaultdict

def step(r, c, op):
    if op == ">":        
        dr, dc = 1, 0 
    elif op == "<":
        dr, dc = -1, 0
    elif op == "^":
        dr, dc = 0, 1
    else:
        dr, dc = 0, -1
    return r + dr, c + dc

instructions = input()

def part1(instructions):
    r = c = 0
    s = {(r, c)}
    for op in instructions:
        r, c = step(r, c, op)
        s.add((r, c))
    return len(s)

def part2(instructions):
    dirs = [[0, 0], [0, 0]] 
    s = {(0, 0)}

    for i in range(len(instructions)):
        santa = i % 2
        r, c = step(*dirs[santa], instructions[i])
        dirs[santa][0] = r
        dirs[santa][1] = c
        s.add((r, c))
        
    return len(s)

print(part1(instructions))
print(part2(instructions))
