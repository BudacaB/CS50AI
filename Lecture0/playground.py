with open("maze2.txt") as f:
    contents = f.read()
contents = contents.splitlines()
print(contents)
height = len(contents)
width = max(len(line) for line in contents)
print(height)
print(width)

walls = []
for i in range(height):
    row = []
    for j in range(width):
        try:
            if contents[i][j] == "A":
                start = (i, j)
                row.append(False)
            elif contents[i][j] == "B":
                goal = (i, j)
                row.append(False)
            elif contents[i][j] == " ":
                row.append(False)
            else:
                row.append(True)
        except IndexError:
            row.append(False)
    walls.append(row)

solution = None

print(walls)

for i, row in enumerate(walls):
    for j, col in enumerate(row):
        if col:
            print("█", end="")
        elif (i, j) == start:
            print("A", end="")
        elif (i, j) == goal:
            print("B", end="")
        elif solution is not None and (i, j) in solution:
            print("*", end="")
        else:
            print(" ", end="")
    print()

state = (5, 0)

row, col = state

# All possible actions
candidates = [
    ("up", (row - 1, col)),
    ("down", (row + 1, col)),
    ("left", (row, col - 1)),
    ("right", (row, col + 1))
]

# Ensure actions are valid
result = []
for action, (r, c) in candidates:
    if 0 <= r < height and 0 <= c < width and not walls[r][c]:
        result.append((action, (r, c)))

print(result)