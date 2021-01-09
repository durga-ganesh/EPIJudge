from typing import Optional

from list_node import ListNode
from test_framework import generic_test

# DG O(n) time and O(1) space
def cyclically_right_shift_list(L: ListNode, k: int) -> Optional[ListNode]:
    def lenL(head: ListNode) -> int:
        count = 1
        while head.next:
            head = head.next
            count += 1
        return count, head

    if not L: return L
    count, tail = lenL(L)
    k = (k % count)
    if k == 0: return L

    head = L
    for _ in range(count - k - 1):
        head = head.next
    
    # patch the two halves
    tail.next = L
    L = head.next
    head.next = None
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('list_cyclic_right_shift.py',
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
