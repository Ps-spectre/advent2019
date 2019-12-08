from collections import Counter

a = [int(x) for x in input().strip()]

W = 25
H = 6


def get_layers(a, w, h):
    total = w * h
    return [a[i:i+total] for i in range(0, len(a), total)]


def part1(a, w, h):
    layers = get_layers(a, w, h)
    l = min(layers, key=lambda x: x.count(0))
    return l.count(1) * l.count(2)


def part2(a, w, h):
    layers = get_layers(a, w, h)
    res = []
    for i in range(len(layers[0])):
        l = 0
        while layers[l][i] == 2:
            l += 1
        res.append(layers[l][i])

    for i, px in enumerate(res):
        sym = " "
        if px == 1: sym = "%"
        print(sym, end='')
        if (i+1) % w == 0: print()
    print()


print(part1(a, W, H))
part2(a, W, H)
