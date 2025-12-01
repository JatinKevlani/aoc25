def solve(filename: str):
    pos = 50
    count_part1 = 0

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            direction = line[0]
            distance = int(line[1:])

            step = 1 if direction == 'R' else -1

            for _ in range(distance):
                pos = (pos + step) % 100

            if pos == 0:
                count_part1 += 1

    return count_part1


if __name__ == "__main__":
    p1 = solve("D:/aoc/day1/input.txt")
    print("Part 1 Password:", p1)
    