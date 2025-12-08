from math import inf

def solve():
    points = []
    with open("D:/aoc25/day8/input.txt") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            x, y, z = map(int, line.split(","))
            points.append((x, y, z))

    n = len(points)

    edges = []
    for i in range(n):
        x1, y1, z1 = points[i]
        for j in range(i + 1, n):
            x2, y2, z2 = points[j]
            dx = x1 - x2
            dy = y1 - y2
            dz = z1 - z2
            d2 = dx*dx + dy*dy + dz*dz
            edges.append((d2, i, j))

    edges.sort(key=lambda e: e[0])

    parent = list(range(n))
    size = [1] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]
        return True

    MAX_PAIRS = 1000
    for idx, (_, i, j) in enumerate(edges):
        if idx >= MAX_PAIRS:
            break
        union(i, j)

    comp_sizes = {}
    for i in range(n):
        r = find(i)
        comp_sizes[r] = comp_sizes.get(r, 0) + 1

    sizes = sorted(comp_sizes.values(), reverse=True)

    answer = sizes[0] * sizes[1] * sizes[2]
    print(answer)


if __name__ == "__main__":
    solve()
