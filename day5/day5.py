arr_input = [int(x) for x in input().split(',')]

def add(x, y, z, a, mx=0, my=0):
    dx = a[x] if mx == 0 else x
    dy = a[y] if my == 0 else y
    a[z] = dx + dy


def mul(x, y, z, a, mx=0, my=0):
    dx = a[x] if mx == 0 else x
    dy = a[y] if my == 0 else y
    a[z] = dx * dy


def put(x, z, a):
    a[z] = x


def out(x, a, mx=0):
    dx = a[x] if mx == 0 else x
    print(dx, end='')


def jmp_true(i, x, y, a, mx=0, my=0):
    dx = a[x] if mx == 0 else x
    dy = a[y] if my == 0 else y
    if dx != 0:
        return dy
    else:
        return i + 3


def jmp_false(i, x, y, a, mx=0, my=0):
    dx = a[x] if mx == 0 else x
    dy = a[y] if my == 0 else y
    if dx == 0:
        return dy
    else:
        return i + 3


def less_than(x, y, z, a, mx=0, my=0):
    dx = a[x] if mx == 0 else x
    dy = a[y] if my == 0 else y
    if dx < dy:
        a[z] = 1
    else:
        a[z] = 0


def eq(x, y, z, a, mx=0, my=0):
    dx = a[x] if mx == 0 else x
    dy = a[y] if my == 0 else y
    if dx == dy:
        a[z] = 1
    else:
        a[z] = 0


def do_operation(op, i, a, cmd_input, mx=0, my=0):
    if op == 99:
        return -1
    elif op == 1:
        add(a[i+1], a[i+2], a[i+3], a, mx, my)
        return i + 4
    elif op == 2:
        mul(a[i+1], a[i+2], a[i+3], a, mx, my)
        return i + 4
    elif op == 3:
        put(cmd_input, a[i+1], a)
        return i + 2
    elif op == 4:
        out(a[i+1], a)
        return i + 2
    elif op == 5:
        return jmp_true(i, a[i+1], a[i+2], a, mx, my)
    elif op == 6:
        return jmp_false(i, a[i+1], a[i+2], a, mx, my)
    elif op == 7:
        less_than(a[i+1], a[i+2], a[i+3], a, mx, my)
        return i + 4
    elif op == 8:
        eq(a[i+1], a[i+2], a[i+3], a, mx, my)
        return i + 4


def part(a, cmd_input=1):
    i = 0
    while i < len(a):
        op = a[i]

        if op > 99:
            s = str(op)
            op = int(s[-2] + s[-1])
            mx = int(s[-3])
            my = 0
            if len(s) >= 4:
                my = int(s[-4])

            di = do_operation(op, i, a, cmd_input, mx, my)
        else:
            di = do_operation(op, i, a, cmd_input)

        if di == -1: break

        i = di

    print()

part(arr_input[:], 1)
part(arr_input[:], 5)
