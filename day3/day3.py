import fileinput
from collections import namedtuple


a = [l.strip().split(',') for l in fileinput.input()]


def make_point(x, y):
    p = namedtuple('Point', 'x y')
    p.x, p.y = x, y
    return p


def make_line(x1, y1, x2, y2, steps):
    p = namedtuple('Line', 'x1 y1 x2 y2 steps')
    p.x1, p.y1, p.x2, p.y2 = x1, y1, x2, y2
    p.steps = steps
    return p


def is_hor(line):
    return line.y1 == line.y2


def get_point(hor, ver):
    px, py = ver.x1, hor.y1
    if px == 0 and py == 0: return
    xs, ys = [hor.x1, hor.x2], [ver.y1, ver.y2]
    xs.sort(), ys.sort()

    if xs[0] <= px <= xs[1] and ys[0] <= py <= ys[1]:
        return make_point(px, py)


def intersect(l1, l2):
    b1, b2 = is_hor(l1), is_hor(l2)
    if b1 == b2: return
    return get_point(l1, l2) if b1 else get_point(l2, l1)


def build_line(command, pos, steps):
    V, val = command[0], int(command[1:])

    if   V == 'R': step = make_point(val, 0)
    elif V == 'L': step = make_point(-val, 0)
    elif V == 'U': step = make_point(0, val)
    elif V == 'D': step = make_point(0, -val)

    line = make_line(pos.x, pos.y, pos.x + step.x, pos.y + step.y, steps)
    steps += val
    pos.x, pos.y = line.x2, line.y2
    return (line, steps)


def man_dist(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)


def all_parts():
    lines = []
    pos, steps = make_point(0, 0), 0

    for command in a[0]:
        line, steps = build_line(command, pos, steps)
        lines.append(line)

    dist, bs = 1 << 32, 1 << 32
    pos, steps = make_point(0, 0), 0

    for command in a[1]:
        line, steps = build_line(command, pos, steps)

        for target_line in lines:
            t = intersect(line, target_line)
            if not t: continue

            # PART1 calculation
            d = abs(t.x) + abs(t.y)
            if d < dist: dist = d

            # PART2 calculation
            s1 = line.steps + man_dist(line.x1, line.y1, t.x, t.y)
            s2 = target_line.steps + man_dist(target_line.x1, target_line.y1, t.x, t.y)
            total = s1 + s2

            if total < bs: bs = total

    return (dist, bs)


part1, part2 = all_parts()
print("part1 = {0}, part2 = {1}".format(part1, part2))
