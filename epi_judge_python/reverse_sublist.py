from typing import Optional

from list_node import ListNode
from test_framework import generic_test

# DG O(n) time and O(1) space - PRAMP
# Also do LC #25: https://leetcode.com/problems/reverse-nodes-in-k-group/
def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    if not L: return L
    dummyHead = subHead = ListNode(next=L)
    cur = L

    for _ in range(start - 1):
        subHead = subHead.next

    prev = subHead.next
    cur = prev.next
    for _ in range(finish - start):
        next = cur.next
        prev.next = next
        cur.next = subHead.next
        subHead.next = cur
        cur = prev.next

    return dummyHead.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
