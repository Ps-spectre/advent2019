import fileinput

a = [l.strip() for l in fileinput.input()]

class OrbitMap:
    def __init__(self):
        self.m = {}
        self.a = []

    def get_index(self, v):
        if v == "COM": return -1

        m, a = self.m, self.a

        i = m.get(v, -1)
        if i >= 0: return i

        a.append(-2)
        i = len(a) - 1
        m[v] = i
        return i

    def add(self, edge):
        a, b = edge.split(')')
        ai = self.get_index(a)
        bi = self.get_index(b)
        self.a[bi] = ai

    def root(self, vi):
        p = self.a[vi]
        path = [p]
        while p != -1:
            p = self.a[p]
            path.append(p)

        return path

    def checksums(self):
        total = 0
        for v in self.m.values():
            path = self.root(v)
            total += len(path)
        return total

    def find(self, v1, v2):
        start_i = self.get_index(v1)
        to_i = self.get_index(v2)
        path1 = set(self.root(start_i))
        path2 = set(self.root(to_i))
        res = path1 ^ path2
        return len(res)

def solution(a):
    orbit = OrbitMap()
    for x in a:
        orbit.add(x)

    print(orbit.checksums())
    print(orbit.find("YOU", "SAN"))


solution(list(a))
