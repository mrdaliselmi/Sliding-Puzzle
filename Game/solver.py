from .node import *
import collections
class Solver:
    """
    An '8-puzzle' solver
    - 'start' is a Puzzle instance
    """
    def __init__(self, start):
        self.start = start

    def solve(self):
        """
        Perform BFS and return a path
        to the solution, if it exists
        """
        queue = collections.deque([Node(self.start)])
        seen = set()
        seen.add(queue[0].state)
        while queue:
            queue = collections.deque(sorted(list(queue), key=lambda node: node.f))
            node = queue.popleft()
            if node.solved:
                return node.path

            for move, action in node.actions:
                child = Node(move(), node, action)

                if child.state not in seen:
                    queue.appendleft(child)
                    seen.add(child.state)
