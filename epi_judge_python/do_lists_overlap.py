import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# DG O(m+n) time and O(1) space PRAMP
def overlapping_lists(l0: ListNode, l1: ListNode) -> Optional[ListNode]:
    if not l0 or not l1: return None

    from is_list_cyclic import has_cycle
    c0, c1 = has_cycle(l0), has_cycle(l1)
    if (c0 and not c1) or (not c0 and c1): # one has cycle & the other don't
        return None
    
    from do_terminated_lists_overlap import overlapping_no_cycle_lists
    if not c0 and not c1: # both don't have cycles
        return overlapping_no_cycle_lists(l0, l1)

    # both have cycles. Maybe overlapping
    if c0 is c1: # overlap is not on the cycle
        h0, h1 = l0, l1
        while True:
            if h0 is h1: return h0
            if h0 is c0.next: h0 = l1
            if h1 is c0.next: h1 = l0 # c0.next
            h0, h1 = h0.next, h1.next
    else:
        # verify if c0 and c1 are on the same cycle
        temp = c0.next
        while temp is not c0:
            if temp is c1: return c0
            temp = temp.next
        return None


@enable_executor_hook
def overlapping_lists_wrapper(executor, l0, l1, common, cycle0, cycle1):
    if common:
        if not l0:
            l0 = common
        else:
            it = l0
            while it.next:
                it = it.next
            it.next = common

        if not l1:
            l1 = common
        else:
            it = l1
            while it.next:
                it = it.next
            it.next = common

    if cycle0 != -1 and l0:
        last = l0
        while last.next:
            last = last.next
        it = l0
        for _ in range(cycle0):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    if cycle1 != -1 and l1:
        last = l1
        while last.next:
            last = last.next
        it = l1
        for _ in range(cycle1):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    common_nodes = set()
    it = common
    while it and id(it) not in common_nodes:
        common_nodes.add(id(it))
        it = it.next

    result = executor.run(functools.partial(overlapping_lists, l0, l1))

    if not (id(result) in common_nodes or (not common_nodes and not result)):
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_lists_overlap.py',
                                       'do_lists_overlap.tsv',
                                       overlapping_lists_wrapper))
