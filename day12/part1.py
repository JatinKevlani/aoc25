with open("D:/aoc25/day12/input.txt") as f:
    data = f.read()

last_block = data.split("\n\n")[-1]
lines = last_block.split("\n")

count = 0

for line in lines:
    parts = line.split(": ")
    size = parts[0].split("x")
    w = int(size[0])
    h = int(size[1])

    nums = parts[1].split(" ")
    total = sum(int(x) * 9 for x in nums)

    if total <= w * h:
        count += 1

print("Part 1: {}".format(count))
