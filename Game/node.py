class Node:
    """
    A class representing a Solver node
    - 'puzzle' is a Puzzle instance representing the current state of the puzzle
    - 'parent' is the parent node this node is generated from (default None)
    - 'action' is the action taken to produce puzzle instance (default None)
    """
    def __init__(self, puzzle, parent=None, action=None):
        self.puzzle = puzzle
        self.parent = parent
        self.action = action
        if (self.parent != None):
            self.g = parent.g + 1
        else:
            self.g = 0

    @property
    def score(self):
        """
        Return the score of the node (f = g + h)
        """
        return (self.g + self.h)

    @property
    def state(self):
        """
        Return a hashable representation of self
        """
        return str(self)

    @property
    def path(self):
        """
        Reconstruct a path from to the root 'parent'
        """
        node, p = self, []
        while node:
            p.append(node)
            node = node.parent
        yield from reversed(p)

    @property
    def solved(self):
        """ Wrapper to check if 'puzzle' is solved """
        return self.puzzle.solved

    @property
    def actions(self):
        """ Wrapper for 'actions' accessible at current state """
        return self.puzzle.actions

    @property
    def h(self):
        """" Heuristic function (Manhattan distance) """
        return self.puzzle.manhattan

    @property
    def f(self):
        """"f"""
        return self.h + self.g

    def __str__(self):
        return str(self.puzzle)
