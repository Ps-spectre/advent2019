from collections import Counter

a = input().strip()

W = 25
H = 6

def get_layers(a, w, h):
    total = w * h
    layers = []
    for i, v in enumerate(a):
        if i == 0 or i % total == 0:
            layers.append(list())
        layers[-1].append(int(v))
    return layers


def part1(a, w, h):
    layers = get_layers(a, w, h)
    counters = []
    for l in layers:
        counters.append(Counter(l))

    c = min(counters, key=lambda x: x[0])
    res = c[1] * c[2]
    return res

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
