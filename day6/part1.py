from math import prod

def solve_part1(filename: str = "input.txt") -> int:
    with open(filename, "r") as f:
        grid = [line.rstrip("\n") for line in f]

    rows = len(grid)
    cols = max(len(row) for row in grid)
    grid = [row.ljust(cols) for row in grid]

    blocks = []
    in_block = False
    start = 0

    for c in range(cols):
        col_has_char = any(grid[r][c] != " " for r in range(rows))
        if col_has_char and not in_block:
            in_block = True
            start = c
        elif not col_has_char and in_block:
            in_block = False
            blocks.append((start, c - 1))
    if in_block:
        blocks.append((start, cols - 1))

    total = 0

    for c1, c2 in blocks:
        numbers = []

        for r in range(rows - 1):
            segment = grid[r][c1:c2 + 1]
            digits = "".join(ch for ch in segment if ch.isdigit())
            if digits:
                numbers.append(int(digits))

        op_segment = grid[rows - 1][c1:c2 + 1]
        operator = None
        if "+" in op_segment:
            operator = "+"
        elif "*" in op_segment:
            operator = "*"
        else:
            raise ValueError(f"No operator found in block {c1}-{c2}")

        if operator == "+":
            result = sum(numbers)
        else:  
            result = prod(numbers)

        total += result

    return total


if __name__ == "__main__":
    ans = solve_part1("D:/aoc25/day6/input.txt")
    print("Part 1 Answer:", ans)
