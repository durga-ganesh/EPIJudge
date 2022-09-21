from test_framework import generic_test

# DG O(n) time and space
def can_form_palindrome(s: str) -> bool:
    import collections
    m = collections.Counter(s)

    oddCount = 0
    for _, val in m.items():
        if val % 2 == 1: oddCount += 1
    return oddCount <= 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
