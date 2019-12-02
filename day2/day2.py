a = [int(x) for x in input().split(',')]

def add(x, y, z, a): a[z] = a[x] + a[y]
def mul(x, y, z, a): a[z] = a[x] * a[y]

def part1(a, noun, verb):
    a[1], a[2] = noun, verb
    for i in range(0, len(a), 4):
        if a[i] == 99: break;
        elif a[i] == 1: add(a[i+1], a[i+2], a[i+3], a)
        elif a[i] == 2: mul(a[i+1], a[i+2], a[i+3], a)
    return a[0]

def part2(a):
    for i in range(0, 100):
        for k in range(0, 100):
            if 19690720 == part1(list(a), i, k): return (i, k)

print(part1(list(a), 12, 2))
noun, verb = part2(list(a))
print(100 * noun + verb)
