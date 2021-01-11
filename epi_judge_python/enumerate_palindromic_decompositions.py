from typing import List

from test_framework import generic_test

# DG O(n*2^n) => T(n) = T(n-1)+T(n-2)+....+T(1)
def palindrome_decompositions(text: str) -> List[List[str]]:
    def is_palindrome(subStr:str) -> bool:
        l = len(subStr)
        return (subStr[:l//2] == subStr[l//2:][::-1]) if l%2==0 \
                else (subStr[:l//2] == subStr[l//2+1:][::-1])
    
    def _helper(L:list, s:str, soFar:list=[]):
        if not s:
            L.append(soFar.copy())
            return
        
        for i in range(1, len(s)+1):
            if is_palindrome(s[:i]):
                _helper(L, s[i:], soFar+[s[:i]])
    L = []
    _helper(L, text)
    return L


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'enumerate_palindromic_decompositions.py',
            'enumerate_palindromic_decompositions.tsv',
            palindrome_decompositions, comp))
