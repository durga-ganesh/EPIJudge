from typing import List

from test_framework import generic_test
import copy

# DG O(n) additional space
def n_queens(n: int) -> List[List[int]]:
    def n_queens_helper(L:list, colMap:list, diagMap45:list,
                        diagMap135:list, row:int=0, soFar:list=[]):
        if row >= n:
            L.append(copy.deepcopy(soFar))
            return
        for col in range(n):
            # place a queen at (row, col) if safe
            if colMap[col] or diagMap45[row+col] or \
                diagMap135[n-1-row+col]:
                continue
            colMap[col] = diagMap45[row+col] = diagMap135[n-1-row+col] = True
            soFar.append(col)

            # next row
            n_queens_helper(L, colMap, diagMap45, diagMap135, row+1, soFar)

            # back-track
            soFar.pop()
            colMap[col] = diagMap45[row+col] = diagMap135[n-1-row+col] = False

    if n <= 0: return []  
    L = []
    colMap     = [False] * n
    diagMap45  = [False] * (2*n-1)
    diagMap135 = [False] * (2*n-1)
    n_queens_helper(L, colMap, diagMap45, diagMap135)
    return L


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('n_queens.py', 'n_queens.tsv', n_queens,
                                       comp))
