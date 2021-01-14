from typing import Iterator, List

from test_framework import generic_test
import heapq

# O(nlogk) time and O(k) (for heap)
def sort_approximately_sorted_array(sequence: Iterator[int],
                                    k: int) -> List[int]:
    if k <= 0: return []
    h = []
    for _ in range(k):
        try:
            h.append(next(sequence))
        except:
            return sorted(h)
    heapq.heapify(h)

    L = []
    while h:
        try:
            L.append(heapq.heapreplace(h, next(sequence)))
        except:
            L += sorted(h)
            return L


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
