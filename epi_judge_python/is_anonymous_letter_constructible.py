from test_framework import generic_test

# DG O(m+n) time and space
def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    import collections
    magazineMap = collections.Counter(magazine_text)
    letterMap   = collections.Counter(letter_text)

    for k, v in letterMap.items():
        if v > magazineMap[k]: return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
