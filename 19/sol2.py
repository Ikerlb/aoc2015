def parse(lines):
    molecule = lines.pop()
    lines.pop() # burn
    g = defaultdict(list)
    for line in lines:
        k, v = line.split(" => ")
        g[k].append(v)
    return g, molecule

lines = [line[:-1] for line in stdin]
rules, molecule = parse(lines)


