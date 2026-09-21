# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = None
        nextt = head

        while nextt:
            temp = nextt.next
            nextt.next = curr
            curr, nextt = nextt, temp

        return curr