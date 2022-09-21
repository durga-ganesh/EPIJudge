from typing import List

from test_framework import generic_test

# DG O(n) time and space
def find_nearest_repetition(paragraph: List[str]) -> int:
    dist = len(paragraph)
    m = dict()

    for idx, word in enumerate(paragraph):
        if word in m:
            dist = min(dist, (idx-m[word]))
        m[word] = idx
    return -1 if dist == len(paragraph) else dist


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
