class LRUCache:
    class Node:
        def __init__(self, key, value, next=None, prev=None):
            self.key = key
            self.value = value
            self.next = next
            self.prev = prev

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.start, self.end = self.Node(0, 0), self.Node(0, 0)
        self.start.next, self.end.prev = self.end, self.start

    def remove(self, key):
        if key not in self.cache:
            return
        node = self.cache[key]
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv
        node.prev = node.next = None

    def add(self, node):
        first = self.start.next
        node.next, first.prev = first, node
        self.start.next, node.prev = node, self.start

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(key)
            self.add(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        node = self.Node(key, value)
        if key in self.cache:
            self.remove(key)
            del self.cache[key]

        elif len(self.cache) == self.capacity:
            last = self.end.prev
            self.remove(last.key)
            del self.cache[last.key]

        self.add(node)
        self.cache[key] = node
