from json import loads

d = loads(input())

def dfs1(o):
    if type(o) == list:
        return sum(dfs1(oo) for oo in o)
    elif type(o) == dict:
        return sum(dfs1(oo) for oo in o.values())
    elif type(o) == str:
        return 0
    else:
        return o # should be number

def dfs2(o):
    if type(o) == list:
        s = 0
        for oo in o:
            ss, _ = dfs2(oo)
            s += ss
        return s, False
    elif type(o) == dict:
        s, r = 0, False
        for oo in o.values():
            ss, hr = dfs2(oo)
            s += ss
            r = r or hr
        return 0 if r else s, False 
    elif type(o) == str:
        return 0, o == "red"
    else:
        return o, False

def part1(d):
    return dfs1(d)

def part2(d):
    s, hr = dfs2(d)
    if hr:
        return 0
    return s

print(part1(d))
print(part2(d))
