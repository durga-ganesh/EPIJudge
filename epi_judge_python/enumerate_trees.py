import functools
from typing import List, Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# DG refer to textbook - Complexity PRAMP
def generate_all_binary_trees(num_nodes: int
                              ) -> List[Optional[BinaryTreeNode]]:
    if num_nodes == 0:
        return [None]
    L = []
    for lNodes in range(num_nodes):
        leftL  = generate_all_binary_trees(lNodes)
        rightL = generate_all_binary_trees(num_nodes-lNodes-1)

        for lBinTree in leftL:
            for rBinTree in rightL:
                root = BinaryTreeNode(left=lBinTree, right=rBinTree)
                L.append(root)
    return L


def serialize_structure(tree):
    result = []
    q = [tree]
    while q:
        a = q.pop(0)
        result.append(0 if not a else 1)
        if a:
            q.append(a.left)
            q.append(a.right)
    return result


@enable_executor_hook
def generate_all_binary_trees_wrapper(executor, num_nodes):
    result = executor.run(
        functools.partial(generate_all_binary_trees, num_nodes))

    return sorted(map(serialize_structure, result))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('enumerate_trees.py',
                                       'enumerate_trees.tsv',
                                       generate_all_binary_trees_wrapper))
