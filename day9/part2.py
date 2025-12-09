import math

tiles_x = []
tiles_y = []

with open("D:/aoc25/day9/input.txt") as f:
    for line in f.read().strip().split("\n"):
        parts = line.split(",")
        tiles_x.append(int(parts[0]))
        tiles_y.append(int(parts[1]))

tile_count = len(tiles_x)

lines = []
for index in range(tile_count):
    next_index = (index + 1) % tile_count

    x1 = tiles_x[index]
    y1 = tiles_y[index]
    x2 = tiles_x[next_index]
    y2 = tiles_y[next_index]

    if x1 == x2:
        if y1 <= y2:
            lines.append([x1, x2, y1, y2])
        else:
            lines.append([x1, x2, y2, y1])
    else:
        if x1 < x2:
            lines.append([x1, x2, y1, y2])
        else:
            lines.append([x2, x1, y1, y2])

max_index = tile_count - 1

largest_area_red_and_green_tiles = 0

for i in range(tile_count):
    for j in range(i + 1, tile_count):
        x1 = tiles_x[i]
        y1 = tiles_y[i]
        x2 = tiles_x[j]
        y2 = tiles_y[j]

        area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)

        if area <= largest_area_red_and_green_tiles:
            continue

        left = min(x1, x2)
        right = max(x1, x2)
        bottom = min(y1, y2)
        top = max(y1, y2)

        inside = True
        for line in lines:
            if line[1] > left and line[0] < right and line[3] > bottom and line[2] < top:
                inside = False
                break

        if inside:
            largest_area_red_and_green_tiles = area

print(f"Part 2: {largest_area_red_and_green_tiles}")
