from sys import stdin

presents = []
for line in stdin:
    l, w, h = map(int, line[:-1].split("x"))
    presents.append((l, w, h))

def area(side1, side2):
    return side1 * side2

def perimeter(side1, side2):
    return 2 * side1 + 2 * side2

def part1(presents):
    s = 0
    for l, w, h in presents:    
        a1 = area(l, w)
        a2 = area(w, h)
        a3 = area(h, l)
        s += (2 * a1) + (2 * a2) + (2 * a3)
        s += min(a1, a2, a3)
    return s

def part2(presents):
    s = 0
    for l, w, h, in presents:
        p1 = perimeter(l, w)
        p2 = perimeter(w, h)
        p3 = perimeter(h, l)
        s += min(p1, p2, p3)
        s += l * w * h
    return s

print(part1(presents))
print(part2(presents))
