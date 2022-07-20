from sys import stdin

def decode(s):
    res = []
    escape = False
    hexa = 0
    h = 0
    for c in s:
        if hexa == 2:
            hexa -= 1
            h = int(c, 16)
        elif hexa == 1:
            hexa -= 1
            res.append(chr(h * 16 + int(c, 16))) 
        elif escape is True and c == "x":
            hexa = 2    
            escape = False
        elif escape is True:
            res.append(c)
            escape = False
        elif c == "\\":
            escape = True
        else:
            res.append(c)
    return "".join(res[1:-1])

def encode(s):
    res = ['"']
    for c in s:
        if c == '"':         
            res.append('\\"')    
        elif c == "\\":
            res.append('\\\\') 
        else: 
            res.append(c)
    res.append('"')
    return "".join(res)

def part1(lines):
    return sum(len(line) - len(decode(line)) for line in lines)

def part2(lines):
    return sum(len(encode(line)) - len(line) for line in lines)

lines = [line[:-1] for line in stdin]

print(part1(lines))
print(part2(lines))
