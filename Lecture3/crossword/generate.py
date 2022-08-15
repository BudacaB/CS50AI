import copy
import sys

from crossword import *


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        w, h = draw.textsize(letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        # TODO - remove
        test_dict = {
            Variable(0, 1, 'across', 3): 'tes',
            # Variable(4, 1, 'across', 4): 'yizz',
            # Variable(1, 4, 'down', 4): 'buzz',
            # Variable(0, 1, 'down', 5): 'testy'
        }
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        temp_domains = copy.deepcopy(self.domains)
        for variable in self.domains.copy():
            for word in self.domains[variable]:
                if len(word) != variable.length:
                    temp_domains[variable].remove(word)
        self.domains = temp_domains

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        revised = False
        if self.crossword.overlaps[x, y] is not None:
            x_overlap_index = self.crossword.overlaps[x, y][0]
            y_overlap_index = self.crossword.overlaps[x, y][1]

            y_overlap_letters = set()
            for word in self.domains[y]:
                y_overlap_letters.add(word[y_overlap_index])

            temp_domains = copy.deepcopy(self.domains)
            for word in self.domains[x]:
                if word[x_overlap_index] not in y_overlap_letters:
                    temp_domains[x].remove(word)
                    revised = True
            self.domains = temp_domains
        return revised

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        if arcs is None:
            arcs = [k for k, v in self.crossword.overlaps.items() if v is not None]
        while len(arcs) != 0:
            arc = arcs.pop()
            if self.revise(arc[0], arc[1]):
                if len(self.domains[arc[0]]) == 0:
                    return False
                neighbors = self.crossword.neighbors(arc[0])
                neighbors.remove(arc[1])  # remove the other node of the current arc
                if neighbors is not None:
                    for variable in neighbors:
                        arcs.append((variable, arc[0]))
        return True

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        if len(assignment) != 0:
            assignment_vars = list(assignment.keys())
            for var in self.crossword.variables:
                if var not in assignment_vars:
                    return False
            for key, value in assignment.items():
                if key not in self.crossword.variables or value is None or value == "":
                    return False
        else:
            return False
        return True

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        words = []
        for key, value in assignment.items():
            if key.length != len(value):
                return False
            neighbors = self.crossword.neighbors(key)
            for neighbor in neighbors:
                if self.crossword.overlaps[key, neighbor] is not None:
                    key_overlap_index = self.crossword.overlaps[key, neighbor][0]
                    neighbor_overlap_index = self.crossword.overlaps[key, neighbor][1]
                    if value[key_overlap_index] != assignment[neighbor][neighbor_overlap_index]:
                        return False
            words.append(value)
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i] == words[j]:
                    return False
        return True

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        assignment_vars = set(assignment.keys())
        vars_to_check = self.crossword.variables - assignment_vars
        vars_to_check.remove(var)  # remove the var being checked
        values_dict = {el: 0 for el in self.domains[var]}
        if len(vars_to_check) != 0:
            for variable in vars_to_check:
                if self.crossword.overlaps[variable, var] is not None:
                    variable_overlap_index = self.crossword.overlaps[variable, var][0]
                    var_overlap_index = self.crossword.overlaps[variable, var][1]
                    for var_word in self.domains[var]:
                        for variable_word in self.domains[variable]:
                            if variable_word[variable_overlap_index] != var_word[var_overlap_index]:
                                values_dict[var_word] += 1
        values_dict = dict(sorted(values_dict.items(), key=lambda item: item[1]))
        values = list(values_dict.keys())
        return values

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        assignment_vars = set(assignment.keys())
        vars_to_check = self.crossword.variables - assignment_vars

        domain_dict = dict()
        domain_vars = []
        if len(vars_to_check) != 0:
            for var in vars_to_check:
                domain_dict[var] = len(self.domains[var])
            min_val = min(domain_dict.values())
            domain_vars = [k for k, v in domain_dict.items() if v == min_val]

        degree_dict = dict()
        if len(domain_vars) > 1:
            for var in domain_vars:
                degree_dict[var] = len(self.crossword.neighbors(var))
            max_val = max(degree_dict.values())
            degree_vars = [k for k, v in degree_dict.items() if v == max_val]
            return degree_vars[0]
        return domain_vars[0]

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        raise NotImplementedError


def main():
    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
