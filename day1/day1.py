lines = [ int(x.strip()) for x in input().splitlines() ]

def fuel(x):
    return x // 3 - 2

def full(x, s=0):
    while True:
        f = fuel(x)
        if f <= 0:
            return s
        s, x = s + f, f

print(sum([fuel(x) for x in lines]))
print(sum([full(x) for x in lines]))
