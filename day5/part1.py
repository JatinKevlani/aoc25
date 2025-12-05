def parse_input(path):
    with open(path) as f:
        lines = [line.strip() for line in f.readlines()]

    ranges = []
    available = []
    parsing_ranges = True
    for line in lines:
        if line == "":
            parsing_ranges = False
            continue

        if parsing_ranges:
            low, high = map(int, line.split("-"))
            ranges.append((low, high))
        else:
            available.append(int(line))

    return ranges, available


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


def is_fresh(id_val, merged_ranges):
    lo, hi = 0, len(merged_ranges) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        start, end = merged_ranges[mid]
        if start <= id_val <= end:
            return True
        if id_val < start:
            hi = mid - 1
        else:
            lo = mid + 1
    return False


ranges, available_ids = parse_input("D:/aoc25/day5/input.txt")
merged = merge_ranges(ranges)

count_fresh = sum(is_fresh(a, merged) for a in available_ids)

print("Fresh ingredient count:", count_fresh)
