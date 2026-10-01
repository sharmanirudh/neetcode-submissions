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
        old2copy = {None: None}
        curr = head

        while curr:
            if curr not in old2copy:
                old2copy[curr] = Node(curr.val)
            if curr.next not in old2copy:
                old2copy[curr.next] = Node(curr.next.val)
            if curr.random not in old2copy:
                old2copy[curr.random] = Node(curr.random.val)
            old2copy[curr].next = old2copy[curr.next]
            old2copy[curr].random = old2copy[curr.random]
            curr = curr.next

        return old2copy[head]