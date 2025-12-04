def read_grid(filename="D:/aoc25/day4/input.txt"):
    with open(filename, "r") as f:
        return [list(line.strip()) for line in f if line.strip()]

NEIGHBORS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1),
]

def count_adjacent_rolls(grid, r, c):
    rows, cols = len(grid), len(grid[0])
    count = 0
    for dr, dc in NEIGHBORS:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
            count += 1
    return count

def simulate_removal(grid):
    rows, cols = len(grid), len(grid[0])
    total_removed = 0

    while True:
        to_remove = []

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '@':
                    if count_adjacent_rolls(grid, r, c) < 4:
                        to_remove.append((r, c))

        if not to_remove:
            break

        for r, c in to_remove:
            grid[r][c] = '.'

        total_removed += len(to_remove)

    return total_removed

def main():
    grid = read_grid()
    result = simulate_removal(grid)
    print("Part 2 Answer:", result)

if __name__ == "__main__":
    main()
