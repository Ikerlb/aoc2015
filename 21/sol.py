from itertools import combinations, product, chain
from math import inf

#Weapons:    Cost  Damage  Armor
weapons = [
    ("Dagger", 8, 4, 0),
    ("Shortsword", 10, 5, 0),
    ("Warhammer", 25, 6, 0),
    ("Longsword", 40, 7, 0),
    ("Greataxe", 74, 8, 0)
]

#Armor:      Cost  Damage  Armor
armor = [
    ("Leather", 13, 0, 1),
    ("Chainmail", 31, 0, 2),
    ("Splintmail", 53, 0, 3),
    ("Bandedmail", 75, 0, 4),
    ("Platemail", 102, 0, 5)
]

#Rings:      Cost  Damage  Armor
rings = [
    ("Damage +1", 25, 1, 0),
    ("Damage +2", 50, 2, 0),
    ("Damage +3", 100, 3, 0),
    ("Defense +1", 20, 0, 1),
    ("Defense +2", 40, 0, 2),
    ("Defense +3", 80, 0, 3)
]

def combs(l, mn, mx):
    for i in range(mn, mx + 1):
        yield from combinations(l, i)

poss_weaps = list(combs(weapons, 1, 1))
poss_armor = list(combs(armor, 0, 1))
poss_rings = list(combs(rings, 0, 2))

def calc_state(l):
    cost = damage = armor = 0
    for _, c, d, a in l:
        cost += c
        damage += d
        armor += a
    return cost, damage, armor 


def battle(bhp, bd, ba, hp, d, a):
    # boss effective damage
    bed = max(bd - a, 1)
    ped = max(d - ba, 1)

    # in how many rounds does the boss win?
    rs_b = (hp // bed) + int(hp % bd != 0)
    # in how many rounds does the player win?
    rs_p = (bhp // ped) + int(bhp % ped != 0)

    if rs_p <= rs_b:
        return True # player wins!
    return False



def part1(bhp, bd, ba, hp):
    m = inf
    for w, a, r in product(poss_weaps, poss_armor, poss_rings):
        cost, damage, armor = calc_state(chain(w, a, r))
        if battle(bhp, bd, ba, hp, damage, armor):
            m = min(m, cost)
    return m

def part2(bhp, bd, ba, hp):
    m = -inf
    for w, a, r in product(poss_weaps, poss_armor, poss_rings):
        cost, damage, armor = calc_state(chain(w, a, r))
        if not battle(bhp, bd, ba, hp, damage, armor):
            m = max(m, cost)
    return m

bhp = 100
bd  = 8
ba  = 2

print(part1(bhp, bd, ba, 100))
print(part2(bhp, bd, ba, 100))
