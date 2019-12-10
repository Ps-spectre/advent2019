import fileinput
import math

a_input = [l.strip() for l in fileinput.input()]


def find(a, r, c):
    coords = []

    for i, row in enumerate(a):
        for k, column in enumerate(row):
            if i == r and k == c: continue
            if a[i][k] == "#":
                coords.append((i-r, k-c))

    coord = sorted(coords, key=lambda k: [k[1], k[0]])
    coords = coords[::-1]

    sight = set()
    visible = set()
    for p in coords:
        gcd = math.gcd(p[0], p[1])
        pn = (p[0] // gcd, p[1] // gcd)
        if pn not in sight:
            sight.add(pn)
            visible.add(p)

    return (r, c, len(sight), visible)


def part1(a):
    asteroids = []
    for i, row in enumerate(a):
        for k, column in enumerate(row):
            if a[i][k] == "#":
                asteroids.append((i, k))

    all_sights = []
    for asteroid in asteroids:
        all_sights.append(find(a, asteroid[0], asteroid[1]))

    return max(all_sights, key=lambda x: x[2])


_, _, res, _ = part1(a_input)
print(res)

d = """.#..#
.....
#####
....#
...##
    """

d2 = """......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####
"""

d3 = """#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###.
"""

d4 = """.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##
"""

d5 = """.#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#..
"""

a = [x for x in d.strip().split('\n')]
a2 = [x for x in d2.strip().split('\n')]
a3 = [x for x in d3.strip().split('\n')]
a4 = [x for x in d4.strip().split('\n')]
a5 = [x for x in d5.strip().split('\n')]


def test_data():
    r, c, total, _ = part1(a)
    assert total == 8
    r, c, total, _ = part1(a2)
    assert total == 33
    r, c, total, _ = part1(a3)
    assert total == 35
    r, c, total, _ = part1(a4)
    assert total == 210
    r, c, total, _ = part1(a5)
    assert total == 41


test_data()
