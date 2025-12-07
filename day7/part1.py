def solve_part1(path: str = "input.txt") -> int:
    grid = open(path).read().splitlines()
    rows, cols = len(grid), len(grid[0])

    start_row = next(r for r in range(rows) if 'S' in grid[r])
    start_col = grid[start_row].index('S')

    splits = 0
    active = {start_col}

    for r in range(start_row + 1, rows):
        new_active = set()
        for c in active:
            ch = grid[r][c]
            if ch == '.':
                new_active.add(c)
            elif ch == '^':
                splits += 1
                if c - 1 >= 0:
                    new_active.add(c - 1)
                if c + 1 < cols:
                    new_active.add(c + 1)
            else:
                raise ValueError(f"Unexpected char {ch!r} at ({r}, {c})")
        active = new_active
        if not active:
            break

    return splits


if __name__ == "__main__":
    ans = solve_part1("D:/aoc25/day7/input.txt")
    print(ans)
