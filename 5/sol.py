from sys import stdin

def window(s, k):
    for i in range(len(s) - (k - 1)):
        yield s[i:i + k]

def is_nice_p1(s):
    vowels = 3 - int(s[0] in "aeiou")
    twice = False
    third = True
    for w in window(s, 2):
        if w[-1] in "aeiou":
            vowels -= 1
        if all(c == w[0] for c in w):
            twice = True
        if w in ["ab", "cd", "pq", "xy"]: 
            third = False
    return vowels <= 0 and twice and third

def is_nice_p2(s):
    prev = None
    rep = set() 
    if not any(w[0] == w[-1] for w in window(s, 3)):
        return False
    d = {}
    for i, w in enumerate(window(s, 2)):
        if w in d and i - d[w] >= 2:
            return True
        elif w not in d:
            d[w] = i    
    return False

def count_nice(words, f):
    return sum(1 for w in words if f(w))

words = []
for line in stdin:
    words.append(line[:-1])

print(count_nice(words, is_nice_p1)) # part 1
print(count_nice(words, is_nice_p2)) # part 2
