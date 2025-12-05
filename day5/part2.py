def merge_ranges(ranges):
    ranges.sort()
    merged = [ranges[0]]

    for start, end in ranges[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end + 1:  
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))
    return merged


ranges = []
with open("D:/aoc25/day5/input.txt") as f:
    for line in f:
        line = line.strip()
        if not line:  
            break
        low, high = map(int, line.split('-'))
        ranges.append((low, high))

merged = merge_ranges(ranges)

answer = sum(high - low + 1 for low, high in merged)
print("Total fresh ingredient IDs:", answer)
