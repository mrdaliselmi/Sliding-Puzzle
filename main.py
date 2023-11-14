import pandas as pd
from Game.puzzle import Puzzle
from Game.solver import Solver
import time
import argparse

def main (): 
    parser = argparse.ArgumentParser(description="Solve a puzzle.")
    parser.add_argument("--h", type=str, default=0, help="Specify the heuristic to use. 0 for Hamming, 1 for Manhattan.")
    args = parser.parse_args()

    shuffling_values = [10,20,30, 40, 50]
    puzzle_sizes = [4,5,6,7,8,9,10]


    results = []

    for size in puzzle_sizes:
        for shuffle in shuffling_values:
            board = [[i + j * size for i in range(1, size + 1)] for j in range(size)]
            board[-1][-1] = 0
            puzzle = Puzzle(board)
            puzzle = puzzle.shuffle(shuffle)
            print("Initial state:")
            puzzle.display()
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
            results.append([size, shuffle, steps, toc - tic, args.h])

        df = pd.DataFrame(results, columns=["size", "shuffling", "steps", "time", "heuristic"])
        df.to_csv("results1.csv", mode="a", header=False,index=False)




if __name__ == "__main__":
    main()
    