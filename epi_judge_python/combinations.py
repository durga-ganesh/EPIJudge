from typing import List

from test_framework import generic_test, test_utils

# DG O(nCk) time PRAMP
def combinations(n: int, k: int) -> List[List[int]]:
    def combinations_helper(L:list, nums:list, soFar:list=[]):
        if len(soFar) == k:
            L.append(soFar.copy())
            return
        if not nums: return

        if (k-len(soFar)) <= len(nums[1:]): # TRICK
            combinations_helper(L, nums[1:], soFar)
        combinations_helper(L, nums[1:], soFar+[nums[0]])

    L = []
    combinations_helper(L, range(1, n+1))
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'combinations.py',
            'combinations.tsv',
            combinations,
            comparator=test_utils.unordered_compare))
