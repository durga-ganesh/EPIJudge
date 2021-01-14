from typing import Iterator, List

from test_framework import generic_test
import heapq

# DG O(nlogn) time and O(n) space.
def online_median(sequence: Iterator[int]) -> List[float]:
    maxHeap, minHeap = [], []

    L = []
    for num in sequence:
        heapq.heappush(maxHeap, -heapq.heappushpop(minHeap, num))

        if len(maxHeap) > len(minHeap):
            heapq.heappush(minHeap, -heapq.heappop(maxHeap))
        
        L.append((-maxHeap[0]+minHeap[0])/2 \
                if len(minHeap) == len(maxHeap) else minHeap[0])

    return L
    '''
    minHeap, maxHeap = [float('inf')], [float('inf')]

    L = []
    for num in sequence:
        if num >= minHeap[0]:
            heapq.heappush(minHeap, num)
        else:
            heapq.heappush(maxHeap, -num)

        l1, l2 = len(maxHeap), len(minHeap)
        if abs(l1-l2) > 1: # rebalance
            if l1 > l2:
                heapq.heappush(minHeap, -heapq.heappop(maxHeap))
            else:
                heapq.heappush(maxHeap, -heapq.heappop(minHeap))

        l1, l2 = len(maxHeap), len(minHeap)
        if l1 == l2:
            L.append((-maxHeap[0]+minHeap[0])/2)
        elif l1 > l2:
            L.append(-maxHeap[0])
        else:
            L.append(minHeap[0])
    
    return L
    '''


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('online_median.py', 'online_median.tsv',
                                       online_median_wrapper))
