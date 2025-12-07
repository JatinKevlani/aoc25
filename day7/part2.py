def solve_part2(path: str = "input.txt") -> int:
    grid = open(path).read().splitlines()
    rows, cols = len(grid), len(grid[0])

    start_row = next(r for r in range(rows) if 'S' in grid[r])
    start_col = grid[start_row].index('S')

    counts = {start_col: 1}

    for r in range(start_row + 1, rows):
        next_counts = {}
        for c, cnt in counts.items():
            if cnt == 0:
                continue

            ch = grid[r][c]
            if ch == '.':
                next_counts[c] = next_counts.get(c, 0) + cnt
            elif ch == '^':
                if c - 1 >= 0:
                    next_counts[c - 1] = next_counts.get(c - 1, 0) + cnt
                if c + 1 < cols:
                    next_counts[c + 1] = next_counts.get(c + 1, 0) + cnt
            else:
                raise ValueError(f"Unexpected char {ch!r} at ({r}, {c})")

        counts = next_counts
        if not counts:
            break

    total_timelines = sum(counts.values())
    return total_timelines


if __name__ == "__main__":
    ans = solve_part2("D:/aoc25/day7/input.txt")
    print(ans)
