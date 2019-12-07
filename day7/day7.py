import itertools

def add(x, y, z, a, mx=0, my=0):
    dx = a[x] if mx == 0 else x
    dy = a[y] if my == 0 else y
    a[z] = dx + dy


def mul(x, y, z, a, mx=0, my=0):
    dx = a[x] if mx == 0 else x
    dy = a[y] if my == 0 else y
    a[z] = dx * dy


def put(in_cmd, z, a):
    a[z] = in_cmd.pop(0)


def out(out_cmd, x, a, mx=0):
    dx = a[x] if mx == 0 else x
    out_cmd.append(dx)


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


def do_operation(op, i, a, in_cmd, out_cmd, mx=0, my=0):
    if op == 99:
        return -1
    elif op == 1:
        add(a[i+1], a[i+2], a[i+3], a, mx, my)
        return i + 4
    elif op == 2:
        mul(a[i+1], a[i+2], a[i+3], a, mx, my)
        return i + 4
    elif op == 3:
        put(in_cmd, a[i+1], a)
        return i + 2
    elif op == 4:
        out(out_cmd, a[i+1], a)
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


def solution(a, in_cmd, i=0, is_stop=False):
    out_cmd = []
    while i < len(a):
        op = a[i]

        if op > 99:
            s = str(op)
            op = int(s[-2] + s[-1])
            mx = int(s[-3])
            my = 0
            if len(s) >= 4:
                my = int(s[-4])

            di = do_operation(op, i, a, in_cmd, out_cmd, mx, my)
        else:
            di = do_operation(op, i, a, in_cmd, out_cmd)

        if di == -1: return (out_cmd, -1)

        i = di
        if is_stop and len(out_cmd) > 0: break

    return (out_cmd, i)


def part1():
    numbers = [0, 1, 2, 3, 4]

    all_res = []
    for p in itertools.permutations(numbers):
        seq = list(p)
        in2 = 0
        for x in seq:
            out_cmd, p = solution(list(a), [x, in2])
            in2 = out_cmd[0]
        all_res.append(in2)

    print(max(all_res))


def part2():
    numbers = [9, 8, 7, 6, 5]
    res = []

    for p in itertools.permutations(numbers):
        seq = list(p)
        input_signals = [ [x] for x in seq ]
        input_signals[0].append(0)

        controllers = [list(a) for x in range(5)]
        pointers = [ 0 for x in range(5)]

        is_run = True
        while is_run:
            for i, con in enumerate(controllers):
                in_cmd = input_signals[i]
                pointer = pointers[i]

                out_cmd, p = solution(con, in_cmd, pointer, True)
                if p == -1:
                    is_run = False
                    break
                next_con = i + 1
                if next_con >= len(controllers):
                    next_con = 0

                input_signals[next_con].extend(out_cmd)
                pointers[i] = p

        res.append(input_signals[0][0])

    print(max(res))


a = [int(x) for x in input().split(',')]

part1()
part2()
