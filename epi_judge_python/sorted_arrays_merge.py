from typing import List

from test_framework import generic_test
import heapq

# DG O(n*logk) k lists and n elements
def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    arr = [(L[0], i, 0) for i, L in enumerate(sorted_arrays) if L]
    heapq.heapify(arr)

    L = []
    while arr:
        smallest_val, list_idx, val_idx = heapq.heappop(arr)
        L.append(smallest_val)
        if (val_idx+1) < len(sorted_arrays[list_idx]): # careful
            heapq.heappush(arr, \
                (sorted_arrays[list_idx][val_idx+1], list_idx, val_idx+1))
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
