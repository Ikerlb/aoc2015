from sys import stdin
from collections import defaultdict
import re
from math import inf

# fly speed in km / s
# fly duration in seconds
# rest duration in seconds
def kms(seconds, fs, fd, rd):
    d, m = divmod(seconds, fd + rd)
    return (d * fd * fs) + (min(m, fd) * fs)

def winners(second, reindeers):
    by_kms = defaultdict(list)
    m = -inf
    for r, chars in reindeers.items():
        km = kms(second, *chars)
        by_kms[km].append(r)
        m = max(m, km)
    return by_kms[m]

def parse(line):
    regex = "(.+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds."
    name, fs, fd, rd = re.match(regex, line).groups()
    return (name, int(fs), int(fd), int(rd))

reindeers = {}
for line in stdin:
    n, fs, fd, rd = parse(line)
    reindeers[n] = (fs, fd, rd)

def part1(reindeers, seconds):
    return max(kms(seconds, *reindeers[r]) for r in reindeers)

def part2(reindeers, seconds):
    scores = defaultdict(int)
    for i in range(1, seconds + 1):
        for w in winners(i, reindeers):
            scores[w] += 1    
    return max(scores.values())

print(part1(reindeers, 2503))
print(part2(reindeers, 2503))
