from typing import List

from test_framework import generic_test

# DG O(m*n) time and O(m+n) space
def fill_surrounded_regions(G: List[List[str]]) -> None:
    def DFS(G, x, y, visited=set()):
        if (x, y) in visited: return
        if not (0 <= x < len(G) and 0 <= y < len(G[0])): return
        if G[x][y] == 'B': return

        visited.add((x, y))
        for (_x, _y) in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            DFS(G, _x, _y, visited)

    if not G or not G[0]: return
    m, n = len(G), len(G[0])
    visited = set()
    for r in range(m):
        DFS(G, r, 0, visited)
        DFS(G, r, n-1, visited)
    for c in range(n):
        DFS(G, 0, c, visited)
        DFS(G, m-1, c, visited)
    
    for r in range(m):
        for c in range(n):
            if G[r][c] == 'W' and (r, c) not in visited:
                G[r][c] = 'B'


def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_enclosed_regions.py',
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))
