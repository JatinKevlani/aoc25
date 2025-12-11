from collections import deque

outputs = {}
with open("D:/aoc25/day11/input.txt") as f:
    for line in f.read().strip().split("\n"):
        parts = line.split(": ")
        outputs[parts[0]] = parts[1].split(" ")

cached_paths = {}

def paths_between(start, end):
    if start == end:
        return 1
    if start == "out":
        return 0
    key = start + end
    if key in cached_paths:
        return cached_paths[key]
    paths = 0
    for output in outputs.get(start, []):
        paths += paths_between(output, end)
    cached_paths[key] = paths
    return paths

queue = deque(["svr"])
first_midpoint = ""
while queue:
    device = queue.popleft()
    if device == "dac":
        first_midpoint = "dac"
        break
    if device == "fft":
        first_midpoint = "fft"
        break
    for output in outputs.get(device, []):
        queue.append(output)

second_midpoint = "fft" if first_midpoint == "dac" else "dac"

print(
    "Part 2:",
    paths_between("svr", first_midpoint)
    * paths_between(first_midpoint, second_midpoint)
    * paths_between(second_midpoint, "out")
)
