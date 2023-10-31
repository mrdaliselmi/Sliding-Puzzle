from Game.puzzle import Puzzle
from Game.solver import Solver
import time
    
board = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
puzzle = Puzzle(board)
puzzle = puzzle.shuffle(5)
s = Solver(puzzle)
tic = time.time()
p = s.solve()
toc = time.time()

steps = 0
for node in p:
    print(node.action)
    node.puzzle.display()
    steps += 1

print("Total number of steps: " + str(steps))
print("Total amount of time in search: " + str(toc - tic) + " second(s)")