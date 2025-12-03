def max_jolt(line: str) -> int:
    digits = [int(ch) for ch in line.strip()]
    best = -1
    n = len(digits)

    for i in range(n):
        for j in range(i + 1, n):
            val = 10 * digits[i] + digits[j]
            if val > best:
                best = val

    return best

total = 0
with open("D:/aoc25/day3/input.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        total += max_jolt(line)

print(total)
