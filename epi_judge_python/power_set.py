from typing import List

from test_framework import generic_test, test_utils

# DG O(2^n) time and space
'''
        # power-set with duplicates
        def powerSet(L, nums, pos=0, soFar=[]):
            L.append(copy.copy(soFar))
            
            digitSet = set()
            for i in range(pos, len(nums)):
                if nums[i] not in digitSet:
                    digitSet.add(nums[i])
                    powerSet(L, nums, i+1, soFar+[nums[i]])
            
        L = []
        nums.sort()
        powerSet(L, nums)
        return L
'''
def generate_power_set(input_set: List[int]) -> List[List[int]]:
    def generate_power_set_helper(L:list, input:list, soFar:list=[], pos=0):
        '''
        # Approach 1
        if not input:
            L.append(soFar.copy())
            return
        generate_power_set_helper(L, input[1:], soFar)
        generate_power_set_helper(L, input[1:], soFar+[input[0]])
        '''
        L.append(soFar.copy())
        for i in range(pos, len(input)):
            generate_power_set_helper(L, input, soFar+[input[i]], i+1)

    L = []
    generate_power_set_helper(L, input_set)
    return L

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('power_set.py', 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
