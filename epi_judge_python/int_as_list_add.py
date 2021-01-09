from typing import Optional

from list_node import ListNode
from test_framework import generic_test

# DG O(max(m, n)) time and space 
def add_two_numbers(L1: ListNode, L2: ListNode) -> Optional[ListNode]:
    if not L1 or not L2: return L1 or L2
    dummySum = tailSum = ListNode()

    _carry = 0
    while L1 or L2:
        val1 = L1.data if L1 else 0
        val2 = L2.data if L2 else 0

        _sum = val1 + val2 + _carry
        _carry = (_sum // 10)

        tailSum.next = ListNode(data=(_sum%10))
        tailSum = tailSum.next

        if L1: L1 = L1.next
        if L2: L2 = L2.next

    if _carry != 0:
        tailSum.next = ListNode(data=_carry)
    return dummySum.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_list_add.py',
                                       'int_as_list_add.tsv', add_two_numbers))
