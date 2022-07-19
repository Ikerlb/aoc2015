from sys import stdin
import re


def add(bit, i, delta):
    while i < len(bit):        
        bit[i] += delta
        i += i & (-i)

def query(bit, i):
    res = 0
    while i > 0:
        res += bit[i]
        i -= i & (-i)     
    return res
            
def toggle(grid, r1, c1, r2, c2):
    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            grid[r][c] = 1 - grid[r][c]    

def turn(grid, r1, c1, r2, c2, v):
    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            grid[r][c] = v

def add(grid, r1, c1, r2, c2, delta):
    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            grid[r][c] = max(0, grid[r][c] + delta)

def part1(instructions):
    N = 1000
    grid = [[0 for _ in range(N)] for _ in range(N)]
    for op, r1, c1, r2, c2 in instructions:
        if op == "toggle":
            toggle(grid, r1, c1, r2, c2)                        
        elif op == "turn off":
            turn(grid, r1, c1, r2, c2, 0)
        else:
            turn(grid, r1, c1, r2, c2, 1)
    return sum(sum(row) for row in grid)

def part2(instructions):
    N = 1000
    grid = [[0 for _ in range(N)] for _ in range(N)]
    for op, r1, c1, r2, c2 in instructions:
        if op == "toggle":    
            add(grid, r1, c1, r2, c2, 2)
        elif op == "turn off":
            add(grid, r1, c1, r2, c2, -1)
        else:
            add(grid, r1, c1, r2, c2, 1)
    return sum(sum(row) for row in grid)

instructions = []
for line in stdin:
    regex = r"(toggle|turn off|turn on) (\d+),(\d+) through (\d+),(\d+)\n"
    op, r1, c1, r2, c2 = re.match(regex, line).groups() 
    instructions.append((op, int(r1), int(c1), int(r2), int(c2)))

print(part1(instructions))
print(part2(instructions))

