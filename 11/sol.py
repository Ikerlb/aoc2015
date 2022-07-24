def window(s, k):
    for i in range(len(s) - (k - 1)):
        yield s[i:i + k]

def has_increasing_straight(arr):
    for w in window(arr, 3):
        if w[0] == w[1] - 1 == w[2] - 2:
            return True
    return False

def has_two_pairs(arr):
    p = pi = None        
    for i, w in enumerate(window(arr, 2)):
        if w[0] != w[1]:
            continue
        if p is None:
            pi, p = i, w
        elif p != w or i - pi >= 2:
            return True
    return False

# mutates arr
def increment(arr, c = 1, start_with = None):
    i = len(arr) - 1 if start_with is None else start_with
    while c > 0 and i >= 0:
        c, d = divmod(arr[i] + c, 26)
        arr[i] = d
        i -= 1
    if c > 0 and i < 0:
        arr.insert(0, c - 1)

def is_valid(arr):
    return has_increasing_straight(arr) \
           and has_two_pairs(arr) \
           and all(i not in [8, 11, 14] for i in arr )

def decode(arr):
    return "".join(chr(i + ord('a')) for i in arr)

# mutates arr
def next_valid_word(arr):
    while True:    
        increment(arr)
        if is_valid(arr):
            return

s = list(map(lambda x: ord(x) - ord('a'), input()))

# one very simple optimization
# would be to increment starting at
# the index which has either i, o or l
# but I think I got lucky with my input
# so i'll just leave it like this

next_valid_word(s) # part1
print(decode(s)) 

next_valid_word(s) # part2
print(decode(s)) 
