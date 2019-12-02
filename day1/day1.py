import fileinput

lines = [ int(x.strip()) for x in fileinput.input() ]

def fuel(x): return x // 3 - 2

def full(x, s=0):
    while True:
        f = fuel(x)
        if f <= 0: return s
        s, x = s + f, f

def part1(): return sum([fuel(x) for x in lines])
def part2(): return sum([full(x) for x in lines])

print(part1())
print(part2())
