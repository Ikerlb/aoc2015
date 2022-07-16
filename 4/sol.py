import hashlib

sk = input()

def k_prefix_zeros(digest, k):
    i = 0
    while k >= 2:
        if digest[i] != 0:
            return False
        k -= 2
        i += 1
    if k > 0:
        return digest[i] < 0x10
    return True

def decode(sk, k):
    for nonce in range(10_000_000):
        h = hashlib.md5(bytes(f"{sk}{nonce}", "ascii"))
        if k_prefix_zeros(h.digest(), k):
            return nonce
    return None

def part1(sk):
    return decode(sk, 5)

def part2(sk):
    return decode(sk, 6)

print(part1(sk))
print(part2(sk))
