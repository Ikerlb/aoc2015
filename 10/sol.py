from itertools import groupby

start = input()

def step(s):
    res = []
    for k, g in groupby(s):
        l = list(g)
        res.append(f"{len(l)}{k}")
    return "".join(res)


def look_and_say(line):
    c = 0
    output = ''
    
    while c < len(line):
        num = line[c]
        count = 0

        while c < len(line) and line[c] == num:
            count += 1
            c+=1
        output += (str(count) + num)
    return output

#def _steps(s, k):
#    i = 0
#    while (s1 := look_and_say(s)) == (s2 := step(s)):
#        i += 1
#    return i 

def steps(s, k):
    for _ in range(k):
        s = step(s)
    return s

def steps(s, k, f):
    for _ in range(k):
        s = f(s)
    return s

def lookAndSay(s,x):
    if x ==1:
        return str(len(s))+str(x)
    d = s.split(str(x))
    final = ""
    count = 0
    i = 0
    while i<len(d) and d[i]=="":
        i+=1
    if i>0:
        final+=str(i)+str(x)
    start = i
    while i<len(d):
        if d[i] == "":
            count+=1
        else:
            if i>start:
                final+=str(count+1)+str(x)
                count = 0
            final+=lookAndSay(d[i],x-1)
        i+=1
    if count>0:
        final+=str(count)+str(x)
    return final

#print(len(steps(start, 40))) # part 1
#print(len(steps(start, 50))) # part 2

s1 = steps(start, 16, step)
print(s1, len(s1))
print()
s2 = steps(start, 16, lambda x: lookAndSay(x, 3))
print(s2, len(s2))

print(s1[:378])
print(s2[:378]
print()
print(s1[378:])
print(s2[378:])

#for i, (c1, c2) in enumerate(zip(s1, s2)):
#    print(i, c1, c2)
#    assert(c1 == c2)
