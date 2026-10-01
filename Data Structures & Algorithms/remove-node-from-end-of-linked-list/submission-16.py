# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        node = head
        while node:
            size += 1
            node = node.next

        pos = size - n

        if pos == 0:
            head = head.next
            return head

        node = head
        for i in range(pos - 1):
            node = node.next
        node.next = node.next.next

        return head