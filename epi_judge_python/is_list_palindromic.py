from list_node import ListNode
from test_framework import generic_test

# DG O(n) time and O(1) space
def is_linked_list_a_palindrome(L: ListNode) -> bool:
    if not L or not L.next: return True

    dummyHead = ListNode()
    slow = fast = L
    while fast and fast.next:
        temp = slow
        slow, fast = slow.next, fast.next.next

        temp.next = dummyHead.next
        dummyHead.next = temp
    
    if fast: # Odd length
        slow = slow.next
    
    revL = dummyHead.next
    while slow:
        if revL.data != slow.data:
            return False
        revL, slow = revL.next, slow.next
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
