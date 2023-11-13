class Node:
    def __init__(self, puzzle, parent=None, action=None, flag=0):
        self.puzzle = puzzle
        self.parent = parent
        self.action = action
        if (self.parent != None):
            self.g = parent.g + 1
        else:
            self.g = 0
        self.flag = flag

    @property
    def score(self):
        return (self.g + self.h)

    @property
    def state(self):
        return str(self)

    @property
    def path(self):
        node, p = self, []
        while node:
            p.append(node)
            node = node.parent
        yield from reversed(p)

    @property
    def solved(self):
        return self.puzzle.solved

    @property
    def actions(self):
        return self.puzzle.actions

    @property
    def h(self):
        if self.flag=="1":
            print("Using Manhattan")
            return self.puzzle.manhattan
        else:
            print("Using Hamming")
            return self.puzzle.hamming

    @property
    def f(self):
        return self.h + self.g

    def __str__(self):
        return str(self.puzzle)
