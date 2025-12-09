def read_points(path="D:/aoc25/day9/input.txt"):
    pts = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            x, y = map(int, line.split(","))
            pts.append((x, y))
    return pts

reds = read_points()

best_area = 0

for i in range(len(reds)):
    x1, y1 = reds[i]
    for j in range(i + 1, len(reds)):
        x2, y2 = reds[j]

        width = abs(x1 - x2) + 1
        height = abs(y1 - y2) + 1

        area = width * height
        if area > best_area:
            best_area = area

print(best_area)
