from typing import Optional

from list_node import ListNode
from test_framework import generic_test

# DG O(m+n) time and O(1) space
def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    if not L1 or not L2: return L1 or L2
    dummyHead = dummyTail = ListNode()

    while L1 and L2:
        if L1.data <= L2.data:
            dummyTail.next = L1
            L1 = L1.next
        else:
            dummyTail.next = L2
            L2 = L2.next
        dummyTail = dummyTail.next
    dummyTail.next = L1 or L2
    return dummyHead.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
