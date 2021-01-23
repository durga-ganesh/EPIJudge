from typing import Set

from test_framework import generic_test

# DG graph BFS O(|V|+|E|) time and O(|V|) space
def transform_string(D: Set[str], s: str, t: str) -> int:
    def _neighbors(v, D):
        L = []
        charSeq = 'abcdefghijklmnopqrstuvwxyz'
        [L.append(v[:i]+ch+v[i+1:]) \
            for i in range(len(v)) for ch in charSeq \
            if (v[i] != ch) and v[:i]+ch+v[i+1:] in D]
        return L
    
    queue = [s]
    visited = set([s])
    shortestSeqLen = 0

    while queue:
        qLen = len(queue)
        for _ in range(qLen):
            v = queue.pop(0)
            if v == t:
                return shortestSeqLen
            for _n in _neighbors(v, D):
                if _n not in visited:
                    queue.append(_n)
                    visited.add(_n)
        shortestSeqLen += 1
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_transformability.py',
                                       'string_transformability.tsv',
                                       transform_string))
