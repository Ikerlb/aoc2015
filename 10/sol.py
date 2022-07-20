from itertools import groupby

start = input()

def step(s):
    res = []
    for k, g in groupby(s):
        l = list(g)
        res.append(f"{len(l)}{k}")
    return "".join(res)

def steps(s, k):
    for _ in range(k):
        s = step(s)
    return s

print(len(steps(start, 40))) # part 1
print(len(steps(start, 50))) # part 1
