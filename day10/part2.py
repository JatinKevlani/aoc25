from pulp import *

lines = open("D:/aoc25/day10/input.txt").read().split("\n")
total = 0

for line in lines:
    parts = line.split(" ")
    buttons = parts[1:-1]

    final = tuple(int(x) for x in parts[-1].strip("{}").split(","))
    add_vals = []
    for button in buttons:
        indices = [int(x) for x in button.strip("()").split(",")]
        change = [1 if i in indices else 0 for i in range(len(final))]
        add_vals.append(change)

    prob = LpProblem("aoc", LpMinimize)

    options = len(add_vals)
    press_counts = [
        LpVariable(f"b{i}", lowBound=0, cat="Integer") for i in range(options)
    ]

    prob += lpSum(press_counts)

    for pos in range(len(final)):
        prob += (
            lpSum(press_counts[btn] * add_vals[btn][pos] for btn in range(options))
            == final[pos],
            f"p{pos}",
        )

    prob.solve(PULP_CBC_CMD(msg=0))
    total += sum([int(v.varValue) for v in press_counts])

print(total)
