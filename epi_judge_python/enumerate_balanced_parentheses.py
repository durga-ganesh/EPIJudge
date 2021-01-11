from typing import List

from test_framework import generic_test, test_utils

# DG Check the text book
def generate_balanced_parentheses(num_pairs: int) -> List[str]:

    def _helper(L:list, lCount:int, rCount:int, soFar:str=""):
        if lCount < 0 or rCount < 0 or lCount > rCount:
            return
        
        if lCount == 0 and rCount == 0:
            L.append(soFar)
            return

        _helper(L, lCount-1, rCount, soFar+'(')
        _helper(L, lCount, rCount-1, soFar+')')
    
    L = []
    _helper(L, num_pairs, num_pairs)
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('enumerate_balanced_parentheses.py',
                                       'enumerate_balanced_parentheses.tsv',
                                       generate_balanced_parentheses,
                                       test_utils.unordered_compare))
