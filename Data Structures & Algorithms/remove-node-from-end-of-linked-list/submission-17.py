# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        left, right = dummy, head
        left.next = head

        dist = 0
        while right:
            if dist >= n:
                left = left.next
            right = right.next
            dist += 1
        left.next = left.next.next

        return dummy.next
        