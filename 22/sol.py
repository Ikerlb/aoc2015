from heapq import heappush, heappop

def neighbors(sm, bhp, php, pmp, se, pe, re):
    if pmp >= 53:
        yield sm + 53, bhp - 4, php, pmp - 53, se, pe, re
    if pmp >= 73:
        yield sm + 73, bhp - 2, php + 2, pmp - 73, se, pe, re 
    if pmp >= 113 and se == 0:
        yield sm + 113, bhp, php, pmp - 113, 6, pe, re
    if pmp >= 173 and pe == 0:
        yield sm + 173, bhp, php, pmp - 173, se, 6, re
    if pmp >= 229 and re == 0:
        yield sm + 229, bhp, php, pmp - 229, se, pe, 5

def apply_effects(bhp, bd, php, pmp, pa, se, pe, re, p2):
    if p2:
        php -= 1
    if se > 1:
        se -= 1
        pa = 7
    elif se == 1:
        se -= 1
        pa = 0
    if pe > 0:
        pe -= 1 
        bhp -= 3
    if re > 0:
        re -= 1 
        pmp += 101
    return bhp, php, pmp, pa, se, pe, re

# I hope no one ever finds 
# this very ugly thing I did
def bfs(bhp, bd, php, pmp, p2 = False):
    h = []
    heappush(h, (0, 0, bhp, php, pmp, 0, 0, 0, 0))

    while h:
        sm, turn, bhp, php, pmp, pa, se, pe, re = heappop(h)
        bhp, php, pmp, pa, se, pe, re = apply_effects(bhp, bd, php, pmp, pa, se, pe, re, p2)
        if bhp <= 0:
            return sm
        if php <= 0:
            continue
        if turn == 0:
            for nsm, nbhp, nphp, npmp, nse, npe, nre in neighbors(sm, bhp, php, pmp, se, pe, re):
                heappush(h, (nsm, 1 - turn, nbhp, nphp, npmp, pa, nse, npe, nre))
        else:
            php -= max(bd - pa, 1)
            heappush(h, (sm, 1 - turn, bhp, php, pmp, pa, se, pe, re))

print(bfs(59, 9, 50, 500))
print(bfs(59, 9, 50, 500, p2 = True))
