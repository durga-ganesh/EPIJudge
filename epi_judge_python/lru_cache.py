from test_framework import generic_test
from test_framework.test_failure import TestFailure

class doublyLLNode:
    def __init__(self, key, val, left=None, right=None):
        self.key   = key
        self.val   = val
        self.left  = left
        self.right = right

class doublyLL:
    def __init__(self):
        self.head: doublyLLNode = None
        self.tail: doublyLLNode = None

    def insertAtHead(self, node: doublyLLNode) -> None:
        node.left = node.right = None # reset
        node.right = self.head
        if self.head:
            self.head.left = node
        self.head = node
        if not self.tail:
            self.tail = node
    
    def removeNode(self, node: doublyLLNode) -> None:
        if self.head == node:
            self.head = node.right
        if self.tail == node:
            self.tail = node.left
        if node.right:
            node.right.left = node.left
        if node.left:
            node.left.right = node.right

    def __str__(self):
        s = ""
        node = self.head
        while node:
            s += "[{}, {}] ".format(node.key, node.val)
            node = node.right
        return s

# DG O(1) insert, lookup and erase. O(n) space
# PRAMP we could use an collections.OrderedDict()
class LruCache:
    def __init__(self, capacity: int) -> None:
        self.map   = dict()
        self.ll    = doublyLL()
        self.cap   = capacity
        self.count = 0
        return

    def lookup(self, isbn: int) -> int:
        if isbn not in self.map:
            return -1
        node = self.map[isbn]
        self.ll.removeNode(node)
        self.ll.insertAtHead(node)
        #print("LOOKUP " + str(self.ll))
        return node.val

    def insert(self, isbn: int, price: int) -> None:
        if isbn not in self.map:
            if self.count >= self.cap:
                self.erase(self.ll.tail.key) # evict MRU entry
            llNode = doublyLLNode(isbn, price)
            self.ll.insertAtHead(llNode)
            self.map[isbn] = llNode
            self.count += 1
        else:
            self.lookup(isbn)
        #print("INSERT " + str(self.ll))

    def erase(self, isbn: int) -> bool:
        if isbn not in self.map:
            return False
        llNode = self.map[isbn]
        self.ll.removeNode(llNode)
        self.map.pop(isbn)
        self.count -= 1
        #print("ERASE " + str(self.ll))
        return True


def lru_cache_tester(commands):
    #print(commands)
    if len(commands) < 1 or commands[0][0] != 'LruCache':
        raise RuntimeError('Expected LruCache as first command')

    cache = LruCache(commands[0][1])

    for cmd in commands[1:]:
        if cmd[0] == 'lookup':
            result = cache.lookup(cmd[1])
            if result != cmd[2]:
                raise TestFailure('Lookup: expected ' + str(cmd[2]) +
                                  ', got ' + str(result))
        elif cmd[0] == 'insert':
            cache.insert(cmd[1], cmd[2])
        elif cmd[0] == 'erase':
            result = 1 if cache.erase(cmd[1]) else 0
            if result != cmd[2]:
                raise TestFailure('Erase: expected ' + str(cmd[2]) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unexpected command ' + cmd[0])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lru_cache.py', 'lru_cache.tsv',
                                       lru_cache_tester))
