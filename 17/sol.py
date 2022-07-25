from functools import lru_cache
from sys import stdin
from math import inf

containers = []
for line in stdin:
    containers.append(int(line[:-1]))

containers.sort()

def part1(liters, containers):
    @lru_cache(None)
    def dp(i, s):
        if i == len(containers):
            return int(s == 0)
        if s < 0:
            return 0
        if s == 0:
            return 1
        w  = dp(i + 1, s - containers[i])
        wo = dp(i + 1, s)
        return w + wo
    return dp(0, liters)

def part2(liters, containers):
    # min ways to get s liters
    @lru_cache(None)
    def dp1(i, s):
        if i == len(containers):
            return 0 if s == 0 else inf
        if s < 0:
            return inf
        if s == 0:
            return 0
        w  = dp1(i + 1, s - containers[i]) + 1
        wo = dp1(i + 1, s)
        return min(w, wo)

    @lru_cache(None)
    def dp2(i, s, k):
        if i == len(containers):
            return 1 if k == s == 0 else 0
        if s < 0 or k < 0:
            return 0
        w  = dp2(i + 1, s - containers[i], k - 1)
        wo = dp2(i + 1, s, k)
        return w + wo

    k = dp1(0, liters)
    return dp2(0, liters, k) 

print(part1(150, containers))
print(part2(150, containers))
