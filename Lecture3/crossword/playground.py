import sys

class Variable():

    ACROSS = "across"
    DOWN = "down"

    def __init__(self, i, j, direction, length):
        """Create a new variable with starting point, direction, and length."""
        self.i = i
        self.j = j
        self.direction = direction
        self.length = length
        self.cells = []
        for k in range(self.length):
            self.cells.append(
                (self.i + (k if self.direction == Variable.DOWN else 0),
                 self.j + (k if self.direction == Variable.ACROSS else 0))
            )

    def __hash__(self):
        return hash((self.i, self.j, self.direction, self.length))

    def __eq__(self, other):
        return (
            (self.i == other.i) and
            (self.j == other.j) and
            (self.direction == other.direction) and
            (self.length == other.length)
        )

    def __str__(self):
        return f"({self.i}, {self.j}) {self.direction} : {self.length}"

    def __repr__(self):
        direction = repr(self.direction)
        return f"Variable({self.i}, {self.j}, {direction}, {self.length})"

structure_file = sys.argv[1]
words_file = sys.argv[2]

height = 0
width = 0
structure = []
words = set()

with open(structure_file) as f:
    contents = f.read().splitlines()
    print(contents)
    height = len(contents)
    width = max(len(line) for line in contents)
    structure = []
    for i in range(height):
        row = []
        for j in range(width):
            if j >= len(contents[i]):
                row.append(False)
            elif contents[i][j] == "_":
                row.append(True)
            else:
                row.append(False)
        structure.append(row)

with open(words_file) as f:
    words = set(f.read().upper().splitlines())


# Determine variable set
variables = set()
for i in range(height):
    for j in range(width):

        # Vertical words
        starts_word = (
            structure[i][j]
            and (i == 0 or not structure[i - 1][j])
        )
        if starts_word:
            length = 1
            for k in range(i + 1, height):
                if structure[k][j]:
                    length += 1
                else:
                    break
            if length > 1:
                variables.add(Variable(
                    i=i, j=j,
                    direction=Variable.DOWN,
                    length=length
                ))

        # Horizontal words
        starts_word = (
            structure[i][j]
            and (j == 0 or not structure[i][j - 1])
        )
        if starts_word:
            length = 1
            for k in range(j + 1, width):
                if structure[i][k]:
                    length += 1
                else:
                    break
            if length > 1:
                variables.add(Variable(
                    i=i, j=j,
                    direction=Variable.ACROSS,
                    length=length
                ))

overlaps = dict()
for v1 in variables:
    for v2 in variables:
        if v1 == v2:
            continue
        cells1 = v1.cells
        cells2 = v2.cells
        intersection = set(cells1).intersection(cells2)
        if not intersection:
            overlaps[v1, v2] = None
        else:
            intersection = intersection.pop()
            print(intersection)
            overlaps[v1, v2] = (
                cells1.index(intersection),
                cells2.index(intersection)
            )

test = set(
            v for v in variables
            if v != Variable(0, 1, 'across', 3) and overlaps[v, Variable(0, 1, 'across', 3)]
        )

print(structure)
print(words)
print(variables)
print('-------------------')
print(overlaps)
print('---------------')
print(test)