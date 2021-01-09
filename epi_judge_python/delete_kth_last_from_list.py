from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
# DG O(n) time and O(1) space - sentinal node helps
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    dummyHead = ListNode(next=L)

    first = second = dummyHead
    for _ in range(k):
        second = second.next
    
    while second and second.next:
        first, second = first.next, second.next

    first.next = first.next.next
    return dummyHead.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('delete_kth_last_from_list.py',
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
