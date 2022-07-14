l = input()

def part1(l):
    res = 0
    for c in l:
        if c == "(":
            res += 1
        elif c == ")":
            res -= 1    
    return res

def part2(l):
    res = 0
    for i, c in enumerate(l, 1):
        if c == "(":
            res += 1
        elif c == ")":
            res -= 1
        if res < 0:
            return i
    return None

print(part1(l))
print(part2(l))
