from math import prod

def solve_part2(filename: str = "input.txt") -> int:
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

        for c in range(c1, c2 + 1):
            digits = []
            for r in range(rows - 1):  
                ch = grid[r][c]
                if ch.isdigit():
                    digits.append(ch)

            if digits:
                numbers.append(int("".join(digits)))

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
    ans = solve_part2("D:/aoc25/day6/input.txt")
    print("Part 2 Answer:", ans)
