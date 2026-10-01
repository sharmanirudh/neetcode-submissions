"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        nodes = {}
        i, n = 0, head
        while n:
            nodes[n] = i
            i += 1
            n = n.next

        new_nodes = [Node(0) for _ in range(i)]
        new_head = new_nodes[0]
        for i, n in enumerate(nodes):
            next_idx = nodes[n.next] if n.next is not None else None
            random_idx = nodes[n.random] if n.random is not None else None
            new_nodes[i].val = n.val
            new_nodes[i].next = new_nodes[next_idx] if next_idx is not None else None
            new_nodes[i].random = new_nodes[random_idx] if random_idx is not None else None

        return new_head
