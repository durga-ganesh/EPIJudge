import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK, NONE = range(3)
class GraphVertex:
    def __init__(self) -> None:
        self.d = -1
        self.edges: List[GraphVertex] = []
        self._color = NONE

# DG O(|V|+|E|) time and O(|V|) space
def is_any_placement_feasible(graph: List[GraphVertex]) -> bool:
    def BFS(node: GraphVertex):
        color = WHITE
        node._color = color
        queue = [node]
        
        while queue:
            length = len(queue)
            for _ in range(length):
                v = queue.pop(0)
                color = WHITE if v._color==BLACK else BLACK
                for _n in v.edges:
                    if _n._color == NONE:
                        _n._color = color
                        queue.append(_n)
                    elif _n._color == v._color: return False
        return True
    
    return all([BFS(v) for v in graph if v._color==NONE])
    # PRAMP m-partite graph coloring


@enable_executor_hook
def is_any_placement_feasible_wrapper(executor, k, edges):
    if k <= 0:
        raise RuntimeError('Invalid k value')
    graph = [GraphVertex() for _ in range(k)]

    for (fr, to) in edges:
        if fr < 0 or fr >= k or to < 0 or to >= k:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(is_any_placement_feasible, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_circuit_wirable.py',
                                       'is_circuit_wirable.tsv',
                                       is_any_placement_feasible_wrapper))
