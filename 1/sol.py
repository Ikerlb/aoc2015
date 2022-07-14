l = input()

def solve(l):
    res = 0
    mn = None
    for i, c in enumerate(l, 1):
        res += 1 if c == "(" else -1 
        if res < 0 and mn is None:
            mn = i
    return res, mn


def part1(l):
    res, _ = solve(l)
    return res

def part2(l):
    _, res = solve(l)
    return res

print(part1(l))
print(part2(l))
