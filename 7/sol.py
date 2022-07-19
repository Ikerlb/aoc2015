from collections import deque, defaultdict
from sys import stdin

class Operand:
    def __init__(self, oper):
        if oper.isdigit():
            self.is_num = True    
            self.val = int(oper)
        else:
            self.is_num = False
            self.val = oper

    def get_value(self, context):
        if self.is_num:    
            return self.val
        else:
            return context[self.val]

    def __repr__(self):  
        return f"{self.val}"

def parse(line):
    expr, res = line.split(" -> ")
    if "RSHIFT" in expr: 
        op1, op2 = expr.split(" RSHIFT ")
        return Operand(op1), Operand(op2), "RSHIFT", res
    if "LSHIFT" in expr:
        op1, op2 = expr.split(" LSHIFT ")
        return Operand(op1), Operand(op2), "LSHIFT", res
    if "AND" in expr:
        op1, op2 = expr.split(" AND ")
        return Operand(op1), Operand(op2), "AND", res
    if "OR" in expr:
        op1, op2 = expr.split(" OR ")
        return Operand(op1), Operand(op2), "OR", res
    if "NOT" in expr:
        _, op2 = expr.split(" ")
        return None, Operand(op2), "NOT", res
    return None, Operand(expr), "CONST", res

def build_deps_graph(instructions):
    lhs = defaultdict(list)
    incoming = defaultdict(int)
    for i, (op1, op2, _, out) in enumerate(instructions):
        if op1 is not None and not op1.is_num:
            lhs[op1.val].append(i)
        if op2 is not None and not op2.is_num:
            lhs[op2.val].append(i)

    g = defaultdict(list)
    for i, (op1, op2, _, out) in enumerate(instructions): 
        for lhs_o in lhs[out]:
            g[i].append(lhs_o)
            incoming[lhs_o] += 1

    return g, incoming
        
def toposort(instructions):
    g, incoming = build_deps_graph(instructions)

    q = deque(i for i in range(len(instructions)) if incoming[i] == 0)

    res = []
    while q:
        n = q.popleft()
        res.append(n)
        for nn in g[n]:
            if incoming[nn] == 1:
                q.append(nn)
                del incoming[nn]
            else:
                incoming[nn] -= 1
    return res

instructions = []
for line in stdin:
    line = line[:-1]
    instructions.append(parse(line))
    
def _lshift(a, b):
    return (a << b) & 0xFFFF

def _rshift(a, b):
    return (a >> b) & 0xFFFF

def _and(a, b):
    return (a & b) & 0xFFFF

def _or(a, b):
    return (a | b) & 0xFFFF

def _not(a):
    return (~a) & 0xFFFF 

def _eval(instructions, d):
    for op1, op2, op, out in instructions:
        if out in d:
            continue
        if op == "RSHIFT":
            d[out] = _rshift(op1.get_value(d), op2.get_value(d))
        elif op == "LSHIFT":
            d[out] = _lshift(op1.get_value(d), op2.get_value(d))
        elif op == "AND":
            d[out] = _and(op1.get_value(d), op2.get_value(d))
        elif op == "OR":
            d[out] = _or(op1.get_value(d), op2.get_value(d))
        elif op == "NOT":
            d[out] = _not(op2.get_value(d))
        else:
            d[out] = op2.val
    return d

def eval_context(instructions, d):
    key = "a"
    context = _eval(instructions, d)
    while type(key) != int:
        key = context[key]
    return key

topo = toposort(instructions)
instructions = [instructions[i] for i in topo]

print(p1 := eval_context(instructions, {}))
print(eval_context(instructions, {'b': p1}))
