from typing import List

from test_framework import generic_test, test_utils
import collections

# DG O(n*mlogm) time and O(n) space
def find_anagrams(dictionary: List[str]) -> List[List[str]]:
    m = collections.defaultdict(list)
    for s in dictionary:
        m[''.join(sorted(s))].append(s)
    L = []
    for _, val in m.items():
        if len(val) > 1: L.append(val)
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'anagrams.py',
            'anagrams.tsv',
            find_anagrams,
            comparator=test_utils.unordered_compare))
