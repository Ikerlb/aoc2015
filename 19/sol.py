from sys import stdin
from collections import defaultdict, deque

class Node:
    def __init__(self):
        self.d = {}
        self.word = False

    def __repr__(self):
        res = ",".join(f"{k}:{v}" for k, v in self.d.items())
        return f"({self.word} {res})"

class Trie:
    def __init__(self, words):
        self.root = Node()
        for w in words:
            self.add(w)

    def add(self, w):
        node = self.root
        for c in w:
            if c not in node.d:
                node.d[c] = Node()
            node = node.d[c]
        node.word = True

    def dfs(self, w, n, i, path, res):
        if n.word:
            res.append((i - len(path), path))
        if i == len(w):
            return
        if w[i] in n.d:
            self.dfs(w, n.d[w[i]], i + 1, path + w[i], res)
        

    def report_matches(self, w):
        res = []
        root = self.root
        for i, c in enumerate(w):
            if c in root.d:
                self.dfs(w, root.d[c], i + 1, c, res)
        return res

def divide(s):
    stack = []
    for i in range(len(s) - 1):
        if s[i:i + 2] == "Rn":
            stack.append(i + 2)
        elif s[i:i + 2] == "Ar" and stack:
            yield stack.pop(), i

def parse(mol):
    cur = []
    levels = [cur]
    i = 0
    while i < len(mol):
        if mol[i:i + 2] == "Rn":
            nlevel = []
            cur.append(nlevel)
            levels.append(nlevel)
            cur = nlevel
            i += 2
        elif mol[i:i + 2] == "Ar":
            levels.pop()
            cur = levels[-1]
            i += 2
        else:
            cur.append(mol[i])
            i += 1
    return cur

def flatten(l):
    res = []
    cur = []
    for e in l:
        if type(e) == list:
            res.append("".join(cur))
            cur = []
            res.append(flatten(e))
        else:
            cur.append(e)
    if cur:
        res.append("".join(cur))
    return res

def handle_level(rules, l, depth = 0):
    res = []
    for e in l:
        if type(e) == list:
            res.append("Rn" + handle_level(rules, e, depth + 1) + "Ar")
        else:
            res.append(reduce(rules, e)[1])
    print(f"trying to reduce {depth} {''.join(res)}")
    ret = reduce(rules, "".join(res))[1]
    print(f"finished, {depth} {ret}")
    return ret

def reduce(rules, target):
    q = deque([target])
    s = {target}
    new_rules = defaultdict(list)
    for k, l in rules.items():
        for v in l:
            new_rules[v].append(k)
    trie = Trie(new_rules.keys())
    res = 0
    while q:
        last = step(new_rules, trie, q, s)
        res += 1
    return res, last

def parse_input(lines):
    molecule = lines.pop()
    lines.pop() # burn
    g = defaultdict(list)
    for line in lines:
        k, v = line.split(" => ")
        g[k].append(v)
    return g, molecule

def read_file(name):
    with open(name) as f:
        return f.read().splitlines()

#lines = [line[:-1] for line in stdin]
lines = read_file("input.in")
rules, molecule = parse_input(lines)

# mutates s and q
def step(g, t, q, s):
    for _ in range(len(q)):
        n = q.popleft()
        for i, p in t.report_matches(n):
            for pp in g[p]:
                nn = n[:i] + pp + n[i + len(p):]
                if nn not in s:
                    s.add(nn)
                    q.append(nn)
    return n    

def part1(rules, molecule):
    s = set()
    trie = Trie(rules.keys())
    q = deque([molecule])
    step(rules, trie, q, s)
    
    return len(s)

def part2(rules, molecule):
    #l = ["e"]
    #res = 0
    #while molecule not in s:
    #    print(res)
    #    step(rules, trie, q, s)
    #    res += 1
    #return res
    q = deque([molecule])
    s = {molecule}
    new_rules = defaultdict(list)
    for k, l in rules.items():
        for v in l:
            new_rules[v].append(k)
    trie = Trie(new_rules.keys())
    res = 0
    while "e" not in s:
        step(new_rules, trie, q, s)
        res += 1
        print(len(s))
    return res

#print(part1(rules, molecule))
#print(part2(rules, molecule))


def divide_by_terminal(s, terminal):
    splt = s.split(terminal)
    for ss in splt[:-1]:
        yield ss + terminal
    yield splt[-1]

def reduce_until(rules, terminal, until, s):
    res = 0
    while s != until: 
        nm = []
        for ns in divide_by_terminal(s, terminal):
            steps, last = reduce(rules, ns)
            res += steps
            nm.append(last)
        s = "".join(nm)
        print(s)
    return res



#print(reduce_until(rules, "Ar", "e", molecule))
