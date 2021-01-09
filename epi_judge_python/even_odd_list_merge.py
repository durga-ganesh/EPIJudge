from typing import Optional

from list_node import ListNode
from test_framework import generic_test

# DG O(n) time and O(1) space
def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    if not L: return L
    dummyEven = tailEven = ListNode()
    dummyOdd  = tailOdd  = ListNode()
    
    even = True
    while L:
        if even:
            tailEven.next = L
            tailEven = tailEven.next
        else:
            tailOdd.next = L
            tailOdd = tailOdd.next
        L = L.next
        even = not even

    tailOdd.next  = None
    tailEven.next = None
    tailEven.next = dummyOdd.next
    return dummyEven.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
