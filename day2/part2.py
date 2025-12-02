def is_invalid_part2(n):
    s = str(n)
    if not s or s[0] == '0':
        return False
    length = len(s)
    
    for unit_len in range(1, length // 2 + 1):   
        if length % unit_len == 0:
            unit = s[:unit_len]
            if unit * (length // unit_len) == s:
                return True
    return False

with open("D:/aoc/day2/input.txt") as f:
    data = f.read().strip()

total = 0
for rng in data.split(','):
    start, end = map(int, rng.split('-'))
    for num in range(start, end + 1):
        if is_invalid_part2(num):
            total += num

print("Part 2 Answer:", total)
