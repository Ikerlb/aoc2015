from math import sqrt, floor
from collections import defaultdict

n = int(input())

def multiples(n):
    res = []
    for i in range(1, floor(sqrt(n)) + 1):
        d, m = divmod(n, i)
        #print(n, d, i)
        if m != 0:
            continue
        if d == i:
            res.append(d)
        else:
            res.append(d)
            res.append(i)
    return res

def part1(k):
    i = 0
    while sum(m * 10 for m in multiples(i)) < k:
        i += 1
    return i

def inc(d, k):
    p = d[k]
    d[k] += 1
    return p

def part2(k, t):
    i = 1
    used = defaultdict(int)
    while (s := sum(m * 11 for m in multiples(i) if inc(used, m) <= t)) < k:
        #print(i, s)
        i += 1
    return i

#print(part1(n))
print(part2(n, 50))
