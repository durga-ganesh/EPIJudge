import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class GraphVertex:
    def __init__(self) -> None:
        self.edges: List[GraphVertex] = []
        # Set max_distance = 0 to indicate unvisitied vertex.
        self.max_distance = 0

# DG O(|V|+|E|) time and O(|V|) space PRAMP
def find_largest_number_teams(graph: List[GraphVertex]) -> int:
    def DFS(node: GraphVertex):
        if node.max_distance != 0: return

        for _n in node.edges:
            DFS(_n)
            node.max_distance = max(node.max_distance, 1+_n.max_distance)

    max_len = 0
    for v in graph:
        if v.max_distance == 0:
            DFS(v)
            max_len = max(max_len, v.max_distance)
    return 1+max_len # numNodes in the longest path


@enable_executor_hook
def find_largest_number_teams_wrapper(executor, k, edges):
    if k <= 0:
        raise RuntimeError('Invalid k value')
    graph = [GraphVertex() for _ in range(k)]

    for (fr, to) in edges:
        if fr < 0 or fr >= k or to < 0 or to >= k:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(find_largest_number_teams, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_teams_in_photograph.py',
                                       'max_teams_in_photograph.tsv',
                                       find_largest_number_teams_wrapper))
