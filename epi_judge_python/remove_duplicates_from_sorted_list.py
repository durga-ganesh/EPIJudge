from typing import Optional

from list_node import ListNode
from test_framework import generic_test

# DG O(n) time and O(1) space
def remove_duplicates(head: ListNode) -> Optional[ListNode]:
    if not head: return head
    L = head
    while L and L.next:
        if L.data == L.next.data:
            L.next = L.next.next
        else:
            L = L.next
    return head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'remove_duplicates_from_sorted_list.py',
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
