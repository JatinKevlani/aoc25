def is_invalid_part1(n):
    s = str(n)
    if s[0] == '0':          
        return False
    length = len(s)
    if length % 2 != 0:      
        return False
    half = length // 2
    return s[:half] == s[half:]

with open("D:/aoc/day2/input.txt") as f:
    data = f.read().strip()

total = 0
for rng in data.split(','):
    start, end = map(int, rng.split('-'))
    for num in range(start, end + 1):
        if is_invalid_part1(num):
            total += num

print("Part 1 Answer:", total)
