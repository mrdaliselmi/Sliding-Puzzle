from Game.puzzle import Puzzle
from Game.solver import Solver
import time
import argparse

def main (): 
    parser = argparse.ArgumentParser(description="Solve a puzzle.")
    parser.add_argument("--h", type=str, default=0, help="Specify the heuristic to use. 0 for Hamming, 1 for Manhattan.")
    args = parser.parse_args()
    board = [[1,2,3,4],[5,6, 7,8],[9,10,11,12],[13,14,15,0]]
    # board = [[4, 1, 2], [5, 3, 6], [7, 0, 8]]
    puzzle = Puzzle(board)
    puzzle = puzzle.shuffle(15)
    s = Solver(puzzle, args.h)
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
    
if __name__ == "__main__":
    main()