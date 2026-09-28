# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        n = head
        while n:
            stack.append(n)
            n = n.next

        l = head
        for _ in range(len(stack) // 2):
            r = stack.pop()
            temp = l.next
            l.next = r
            r.next = temp
            l = temp
        l.next = None