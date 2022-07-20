from collections import defaultdict
from sys import stdin
from math import inf

def parse(line):
    ns, w = line.split(" = ")
    src, tgt = ns.split(" to ")
    return src, tgt, int(w)

def create_graph(edges):
    g = defaultdict(list)
    nodes = set()
    for s, t, w in edges:
        g[s].append((t, w))
        g[t].append((s, w))
        nodes.add(s)
        nodes.add(t)
    return g, nodes

def dfs(g, n, v, s, nodes, f, init):
    if nodes == 0:
        return s
    res = init
    for nn, w in g[n]:
        if nn not in v:
            v.add(nn)
            res = f(dfs(g, nn, v, s + w, nodes - 1, f, init), res)
            v.remove(nn)
    return res

def tsp(g, nodes, f, init):
    visited = set()    
    res = init
    for node in nodes: 
        visited.add(node)
        res = f(res, dfs(g, node, visited, 0, len(nodes) - 1, f, init))
        visited.remove(node)
    return res

edges = []
for line in stdin:
    edges.append(parse(line[:-1]))

g, nodes = create_graph(edges)

print(tsp(g, nodes, min, inf)) # part 1
print(tsp(g, nodes, max, -inf)) # part 2
