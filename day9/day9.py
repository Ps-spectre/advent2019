from collections import defaultdict

a = [int(x) for x in input().strip().split(',')]


# 0 - position mode
# 1 - immediate mode
# 2 - relative mode

def get_di(x, mode, rel_base):
    if mode == 2:
        return rel_base[0] + x
    return x


def get_value1(a, x, mode, rel_base):
    if mode == 0:
        return a[x]
    elif mode == 1:
        return x
    elif mode == 2:
        return a[get_di(x, mode, rel_base)]


def get_value2(a, x1, mode1, x2, mode2, rel_base):
    return (get_value1(a, x1, mode1, rel_base),
            get_value1(a, x2, mode2, rel_base))


def add(a, x, y, z, mx, my, mz, rel_base):
    dx, dy = get_value2(a, x, mx, y, my, rel_base)
    a[get_di(z, mz, rel_base)] = dx + dy


def mul(a, x, y, z, mx, my, mz, rel_base):
    dx, dy = get_value2(a, x, mx, y, my, rel_base)
    a[get_di(z, mz, rel_base)] = dx * dy


def put(a, in_cmd, x, mx, rel_base):
    a[get_di(x, mx, rel_base)] = in_cmd.pop(0)


def out(a, out_cmd, x, mx, rel_base):
    dx = get_value1(a, x, mx, rel_base)
    out_cmd.append(dx)
    print(out_cmd)


def jmp_true(a, i, x, y, mx, my, rel_base):
    dx, dy = get_value2(a, x, mx, y, my, rel_base)
    return dy if dx != 0 else i + 3


def jmp_false(a, i, x, y, mx, my, rel_base):
    dx, dy = get_value2(a, x, mx, y, my, rel_base)
    return dy if dx == 0 else i + 3


def less_than(a, x, y, z, mx, my, mz, rel_base):
    dx, dy = get_value2(a, x, mx, y, my, rel_base)
    a[get_di(z, mz, rel_base)] = 1 if dx < dy else 0


def eq(a, x, y, z, mx, my, mz, rel_base):
    dx, dy = get_value2(a, x, mx, y, my, rel_base)
    a[get_di(z, mz, rel_base)] = 1 if dx == dy else 0


def adjust_rel(a, x, mx, rel_base):
    dx = get_value1(a, x, mx, rel_base)
    rel_base[0] += dx


def do_operation(op, i, a, in_cmd, out_cmd, rel_base, mx, my, mz):
    if op == 99:
        return -1
    elif op == 1:
        add(a, a[i+1], a[i+2], a[i+3], mx, my, mz, rel_base)
        return i + 4
    elif op == 2:
        mul(a, a[i+1], a[i+2], a[i+3], mx, my, mz, rel_base)
        return i + 4
    elif op == 3:
        put(a, in_cmd, a[i+1], mx, rel_base)
        return i + 2
    elif op == 4:
        out(a, out_cmd, a[i+1], mx, rel_base)
        return i + 2
    elif op == 5:
        return jmp_true(a, i, a[i+1], a[i+2], mx, my, rel_base)
    elif op == 6:
        return jmp_false(a, i, a[i+1], a[i+2], mx, my, rel_base)
    elif op == 7:
        less_than(a, a[i+1], a[i+2], a[i+3], mx, my, mz, rel_base)
        return i + 4
    elif op == 8:
        eq(a, a[i+1], a[i+2], a[i+3], mx, my, mz, rel_base)
        return i + 4
    elif op == 9:
        adjust_rel(a, a[i+1], mx, rel_base)
        return i + 2


def solution(data, in_cmd, i=0, is_stop=False):
    out_cmd = []
    rel_base = [0]
    a = defaultdict(int)

    for k, v in enumerate(data):
        a[k] = v

    while i < len(data):
        op = a[i]

        if op > 99:
            s = str(op)
            op = int(s[-2] + s[-1])
            mx = int(s[-3])
            my = 0
            mz = 0
            if len(s) >= 4:
                my = int(s[-4])
            if len(s) >= 5:
                mz = int(s[-5])

            di = do_operation(op, i, a, in_cmd, out_cmd, rel_base, mx, my, mz)
        else:
            di = do_operation(op, i, a, in_cmd, out_cmd, rel_base, 0, 0, 0)

        if di == -1: return (out_cmd, -1)

        i = di
        if is_stop and len(out_cmd) > 0: break

    return (out_cmd, i)


def part1():
    out_cmd, p = solution(list(a), [1])
    print(out_cmd)

def part2():
    out_cmd, p = solution(list(a), [2])
    print(out_cmd)


part1()
part2()
