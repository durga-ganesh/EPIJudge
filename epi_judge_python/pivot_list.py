import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# DG O(n) time and O(1) space PRAMP
def list_pivoting(L: ListNode, x: int) -> Optional[ListNode]:
    if not L: return L

    dummyLe = tailLe = ListNode()
    dummyEq = tailEq = ListNode()
    dummyGr = tailGr = ListNode()

    while L:
        if L.data < x:
            tailLe.next = L
            tailLe = tailLe.next
        elif L.data == x:
            tailEq.next = L
            tailEq = tailEq.next
        else:
            tailGr.next = L
            tailGr = tailGr.next
        L = L.next
    
    tailLe.next = tailEq.next = tailGr.next = None
    tailEq.next = dummyGr.next
    tailLe.next = dummyEq.next # Careful

    return dummyLe.next


def linked_to_list(l):
    v = list()
    while l is not None:
        v.append(l.data)
        l = l.next
    return v


@enable_executor_hook
def list_pivoting_wrapper(executor, l, x):
    original = linked_to_list(l)

    l = executor.run(functools.partial(list_pivoting, l, x))

    pivoted = linked_to_list(l)
    mode = -1
    for i in pivoted:
        if mode == -1:
            if i == x:
                mode = 0
            elif i > x:
                mode = 1
        elif mode == 0:
            if i < x:
                raise TestFailure('List is not pivoted')
            elif i > x:
                mode = 1
        else:
            if i <= x:
                raise TestFailure('List is not pivoted')

    if sorted(original) != sorted(pivoted):
        raise TestFailure('Result list contains different values')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pivot_list.py', 'pivot_list.tsv',
                                       list_pivoting_wrapper))
