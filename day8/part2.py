def solve_part2():
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

    edges.sort(key=lambda x: x[0])

    parent = list(range(n))
    size = [1] * n
    sets = n  

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        nonlocal sets
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]
        sets -= 1
        return True

    for _, i, j in edges:
        if union(i, j):
            if sets == 1:
                x1, _, _ = points[i]
                x2, _, _ = points[j]
                print(x1 * x2)  
                return

if __name__ == "__main__":
    solve_part2()
