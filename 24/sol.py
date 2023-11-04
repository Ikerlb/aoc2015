from sys import stdin
from functools import lru_cache, reduce

nums = [int(line[:-1]) for line in stdin]

def two_sum(arr, start, target):
    end = len(arr) - 1
    while start < end:
        sm = arr[start] + arr[end]
        if sm == target:
            yield (arr[start], arr[end])
            # just advance either
            start += 1
        elif sm < target:
            start += 1
        else:
            end -= 1

def ksum(arr, k, start, target):
    if k == 2:
        yield from two_sum(arr, start, target)
        return
    for i in range(start, len(arr) - k + 1):
        yield from ((*tup, arr[i]) for tup in ksum(arr, k - 1, i + 1, target - arr[i]))

def prod(arr):
    res = 1
    for n in arr:
        res *= n
    return res

def ideal_conf(nums, k):
    s = sum(nums)
    target, m = divmod(s, k)

    nums.sort()

    i = 2
    while not (first := list(ksum(nums, i, 0, target))):
        i += 1
    return min(first, key = lambda x: prod(x))

# p1
print(prod(ideal_conf(nums, 3)))

# p2
print(prod(ideal_conf(nums, 4)))
