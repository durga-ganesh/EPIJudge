from typing import List

from test_framework import generic_test

# O(n*logk) time and O(n) space
def sort_k_increasing_decreasing_array(A: List[int]) -> List[int]:
    sorted_arrays = [[]]
    incr = True
    for i in range(len(A)):
        if (i+1) < len(A):
            if incr and A[i] > A[i+1]:
                sorted_arrays.append([A[i]])
                incr = not incr
            elif not incr and A[i] < A[i+1]:
                sorted_arrays.append([A[i]])
                incr = not incr
            else:
                sorted_arrays[-1].append(A[i])
        else:
            sorted_arrays[-1].append(A[i])
    for i in range(len(sorted_arrays)):
        if i % 2 != 0:
            sorted_arrays[i] = sorted_arrays[i][::-1]
    
    from sorted_arrays_merge import merge_sorted_arrays
    return merge_sorted_arrays(sorted_arrays) 


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_increasing_decreasing_array.py',
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))
