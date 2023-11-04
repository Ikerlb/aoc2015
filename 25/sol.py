# given r, c return # of code in processing order

#    |  0   1   2   3   4   5  
# ---+---+---+---+---+---+---+
#  0 |  0   2   5   9  14  20
#  1 |  1   4   8  13  19
#  2 |  3   7  12  18
#  3 |  6  11  17
#  4 | 10  16
#  5 | 15

def index(r, c):
    fst = (r * (r + 1)) // 2
    snd = ((r + c + 1) * (r + c + 2)) // 2
    thd = ((r + 1) * (r + 2)) // 2
    return fst + snd - thd

r, c = map(int, input().split(" "))
res = 20151125
m = 252533
mod = 33554393
for _ in range(index(r, c)):
    res = (res * m) % mod
print(res)
