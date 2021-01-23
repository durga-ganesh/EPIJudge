from typing import List

from test_framework import generic_test
import collections

# DG Graph DFS O(m*n) time and O(m+n) space
def flip_color(x: int, y: int, image: List[List[bool]]) -> None:
    Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))

    def DFS(G, val: bool, src: Coordinate, visited=set()):
        if src in visited: return
        if not (0 <= src.x < len(G) and 0 <= src.y < len(G[0])): return
        if G[src.x][src.y] != val: return

        visited.add(src)
        G[src.x][src.y] = not G[src.x][src.y]
        for _x, _y in [(src.x-1, src.y), (src.x+1, src.y),\
                        (src.x, src.y-1), (src.x, src.y+1)]:
            DFS(G, val, Coordinate(_x, _y), visited)
    
    if not image or not image[0]: return
    DFS(image, image[x][y], Coordinate(x, y))


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_connected_regions.py',
                                       'painting.tsv', flip_color_wrapper))
