from typing import List

from test_framework import generic_test, test_utils
import heapq

# DG O(klogk) time and O(k) space
def k_largest_in_binary_heap(A: List[int], k: int) -> List[int]:
    if not A or k > len(A): return []
    
    maxHeap = [(-A[0], 0)]
    L = []
    for _ in range(k):
        maxVal, idx = heapq.heappop(maxHeap)
        L.append(-maxVal)
        if 2*idx+1 in range(len(A)): # corner-case
            heapq.heappush(maxHeap, (-A[2*idx+1], 2*idx+1))
        if 2*idx+2 in range(len(A)):
            heapq.heappush(maxHeap, (-A[2*idx+2], 2*idx+2))
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'k_largest_in_heap.py',
            'k_largest_in_heap.tsv',
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
