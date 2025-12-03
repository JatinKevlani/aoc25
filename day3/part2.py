def max_12_digits(line: str) -> int:
    digits = [int(ch) for ch in line.strip()]
    take = 12
    result = []

    start = 0
    for chosen in range(take):
        end = len(digits) - (take - chosen)  
        best_digit = -1
        best_index = start

        for i in range(start, end + 1):
            if digits[i] > best_digit:
                best_digit = digits[i]
                best_index = i

        result.append(str(best_digit))
        start = best_index + 1

    return int("".join(result))

total = 0
with open("D:/aoc25/day3/input.txt", "r") as f:
    for line in f:
        if line.strip():
            total += max_12_digits(line)

print("Part 2 - Total Output Joltage:", total)
