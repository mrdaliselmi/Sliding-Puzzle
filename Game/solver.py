from .node import *
import collections
class Solver:
    def __init__(self, start, flag):
        self.start = start
        self.flag = flag

    def solve(self):
        queue = collections.deque([Node(self.start)])
        seen = set()
        seen.add(queue[0].state)
        while queue:
            queue = collections.deque(sorted(list(queue), key=lambda node: node.f))
            node = queue.popleft()
            if node.solved:
                return node.path

            for move, action in node.actions:
                child = Node(move(), node, action, self.flag)

                if child.state not in seen:
                    queue.appendleft(child)
                    seen.add(child.state)
