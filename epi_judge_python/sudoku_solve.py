import copy
import functools
import math
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# DG refer to textbook for complexity
def solve_sudoku(partial_assignment: List[List[int]]) -> bool:
    
    def isSafe(G:List[List[int]], row:int, col:int, val:int) -> bool:
        for r in range(9):
            if G[r][col] == val: return False
        for c in range(9):
            if G[row][c] == val: return False

        r, c = row // 3, col // 3
        for i in range(3*r, 3*(r+1)):
            for j in range(3*c, 3*(c+1)):
                if i == row and j == col: continue
                if G[i][j] == val: return False
        
        return True

    def solve_sudoku_helper(G:List[List[int]], idx:int=0):
        row, col = idx // 9, idx % 9
        if row >= 9 or col >= 9: return True
        
        if G[row][col] != 0:
            return solve_sudoku_helper(G, idx+1)

        for val in range(1, 10):
            if isSafe(G, row, col, val):
                G[row][col] = val
                if solve_sudoku_helper(G, idx+1):
                    return True
                G[row][col] = 0 # back-track
            
        return False
    
    return solve_sudoku_helper(partial_assignment)


def assert_unique_seq(seq):
    seen = set()
    for x in seq:
        if x == 0:
            raise TestFailure('Cell left uninitialized')
        if x < 0 or x > len(seq):
            raise TestFailure('Cell value out of range')
        if x in seen:
            raise TestFailure('Duplicate value in section')
        seen.add(x)


def gather_square_block(data, block_size, n):
    block_x = (n % block_size) * block_size
    block_y = (n // block_size) * block_size

    return [
        data[block_x + i][block_y + j] for j in range(block_size)
        for i in range(block_size)
    ]


@enable_executor_hook
def solve_sudoku_wrapper(executor, partial_assignment):
    solved = copy.deepcopy(partial_assignment)

    executor.run(functools.partial(solve_sudoku, solved))

    if len(partial_assignment) != len(solved):
        raise TestFailure('Initial cell assignment has been changed')

    for (br, sr) in zip(partial_assignment, solved):
        if len(br) != len(sr):
            raise TestFailure('Initial cell assignment has been changed')
        for (bcell, scell) in zip(br, sr):
            if bcell != 0 and bcell != scell:
                raise TestFailure('Initial cell assignment has been changed')

    block_size = int(math.sqrt(len(solved)))
    for i, solved_row in enumerate(solved):
        assert_unique_seq(solved_row)
        assert_unique_seq([row[i] for row in solved])
        assert_unique_seq(gather_square_block(solved, block_size, i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sudoku_solve.py', 'sudoku_solve.tsv',
                                       solve_sudoku_wrapper))
