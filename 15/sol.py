import re
from sys import stdin

class Ingredient:
    def __init__(self, name, cap, d, f, t, cal):
        self.name = name
        self.d = {}
        self.d["capacity"] = cap
        self.d["durability"] = d
        self.d["flavor"] = f
        self.d["texture"] = t
        self.d["calories"] = cal

    def scale(self, mag, d):
        for key in list(d.keys()):
            d[key] += (self.d[key] * mag)

def nums(n, path, res):
    if len(path) == len(ingredients) - 1:
        res.append(path + [n])
        return
    for i in range(1, n):
        path.append(i)
        nums(n - i, path, res)
        path.pop()

def parse(line):
    regex = r"(.+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)"
    name, cap, d, f, t, cal = re.match(regex, line).groups()
    return Ingredient(name, int(cap), int(d), int(f), int(t), int(cal))


def prod(*l):
    r = 1
    for n in l:
        if n < 0:
            n = 0
        r *= n
    return r

def _try(mag, ingredients):
    attr = ["capacity", "durability", "texture", "flavor", "calories"] 
    d = {k:0 for k in attr}
    for m, i in zip(mag, ingredients):
        i.scale(m, d)
    p = prod(d["capacity"], d["durability"], d["texture"], d["flavor"])
    return p, d["calories"]

ingredients = []
for line in stdin:
    ingredients.append(parse(line))

def part1(ingredients):
    path, res = [], []
    nums(100, path, res)
    return max(_try(m, ingredients)[0] for m in res)

def part2(ingredients):
    path, res = [], []
    nums(100, path, res)
    return max(p[0] for m in res if (p := _try(m, ingredients))[1] == 500)

print(part1(ingredients))
print(part2(ingredients))

