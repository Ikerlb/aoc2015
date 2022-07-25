from sys import stdin
from itertools import product

grid = []
for line in stdin:
    #grid.append(list(line[:-1]))
    grid.append([1 if c == "#" else -1 for c in line[:-1]])

def neighbors(grid, r, c):
    g = product([0, -1, 1], repeat = 2)
    next(g)
    for dr, dc in g:
        if not 0 <= r + dr < len(grid):
            continue
        if not 0 <= c + dc < len(grid[0]):
            continue
        yield r + dr, c + dc

# mutates grid
def step(grid):
    for r, c in product(range(len(grid)), range(len(grid[0]))):
        onn = sum(1 for nr, nc in neighbors(grid, r, c) if grid[nr][nc]>0)
        if grid[r][c] == 1:
            grid[r][c] += onn
        else:
            grid[r][c] -= onn
    for r, c in product(range(len(grid)), range(len(grid[0]))):
        if grid[r][c] > 0: # it is on
            grid[r][c] = 1 if grid[r][c] == 3 or grid[r][c] == 4 else -1 
        else:
            grid[r][c] = 1 if grid[r][c] == -4 else -1

def decode(grid):
    res = []
    for row in grid:
        res.append("".join("#" if d == 1 else "." for d in row))
    return "\n".join(res)


def simulate(grid, n, on = []):
    grid = [grid[r][:] for r in range(len(grid))]
    for r, c in on:
        grid[r][c] = 1
    for _ in range(n):
        step(grid)
        for r, c in on:
            grid[r][c] = 1
    return grid

def part1(grid, steps):
    grid = simulate(grid, steps)
    return sum(sum(1 for d in row if d == 1) for row in grid)

def part2(grid, steps):
    grid = simulate(grid, steps, [(0, 0), (0, -1), (-1, 0), (-1, -1)])
    return sum(sum(1 for d in row if d == 1) for row in grid)

print(part1(grid, 100))
print(part2(grid, 100))
