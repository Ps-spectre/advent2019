from collections import defaultdict
a, b = 246515, 739105

def is_valid(p):
    is_pair = False
    for i in range(1, len(p)):
        if p[i-1] > p[i]: return False
        if p[i-1] == p[i]: is_pair = True

    return is_pair


def is_valid2(p):
    if not is_valid(p): return False

    digits = defaultdict(int)
    for c in p:
        digits[c] += 1

    for v in digits.values():
        if v == 2: return True

    return False


def part(lo, hi, valid_fn):
    res = []
    for i in range(lo, hi+1):
        if valid_fn(str(i)):
            res.append(i)
    return len(res)


print(part(a, b, is_valid))
print(part(a, b, is_valid2))
