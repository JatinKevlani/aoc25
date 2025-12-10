from collections import deque


lines = open("D:/aoc25/day10/input.txt").read().split("\n")
total = 0


for line in lines:
    parts = line.split(" ")
    end = parts[0]
    buttons = parts[1:-1]
    buttons = [[int(x) for x in idx_set.strip("()").split(",")] for idx_set in parts[1:-1]]

    final = [char == "#" for char in end[1:-1]]
    state = [False] * len(final)

    q = deque(((state, 0),))
    visited = set(str(state))


    while q:
        curr_state, depth = q.popleft()

        if curr_state == final:
            total += depth
            break
        for button in buttons:
            new_state = curr_state[:]
            for press in button:
                new_state[press] = not new_state[press]
            to_add = new_state

            if str(to_add) not in visited:
                visited.add(str(to_add))
                q.append((to_add, depth + 1))

print(total)