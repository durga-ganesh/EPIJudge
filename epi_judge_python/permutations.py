from typing import List

from test_framework import generic_test, test_utils
import copy

# DG O(n!) time and O(n) stack space
'''
        # Permutations with duplicates 
        def recursiveStep(L, nums, soFar=[]):
            if not nums:
                L.append(copy.copy(soFar))
                return
            
            digitSet = set()
            for i, d in enumerate(nums):
                if d not in digitSet:
                    digitSet.add(d)
                    recursiveStep(L, nums[:i]+nums[i+1:], soFar+[d])
            return
        
        L = []
        recursiveStep(L, nums)
        return L
'''
def permutations(A: List[int]) -> List[List[int]]:
    def permutations_helper(L:list, vals:list, soFar:list=[]):
        if not vals:
            L.append(copy.deepcopy(soFar))
            return

        for i, val in enumerate(vals):
            permutations_helper(L, vals[:i]+vals[i+1:], soFar+[val])
    L = []
    if not A: return L
    permutations_helper(L, A)
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
