from sys import stdin
import re
from collections import defaultdict
from itertools import permutations, chain


def parse(d, line):
    regex = r"(.+) would (lose|gain) (\d+) happiness units by sitting next to (.+)."
    s, op, mag, t = re.match(regex, line).groups()
    sgn = -1 if op == "lose" else 1
    d[(s, t)] = sgn * int(mag)

d = defaultdict(int)
for line in stdin:
    parse(d, line)
    
people = set(c for k in d for c in k)

def cost(p, d):
    n = len(p)
    return sum(d[(p[i], p[(i+1) % n])] + d[(p[i], p[i-1])] for i in range(n))


# well since part2 ran kinda slow
# I'm thinking we could remove some
# time from all the symmetry the table
# being a circule grants. 
# it makes it so that part2 still runs
# kinda fast

print(max(cost(p, d) for p in permutations(people)))
print(max(cost(p, d) for p in permutations(people | {"Me"})))
