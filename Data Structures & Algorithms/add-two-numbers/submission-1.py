# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode()
        carry = 0
        while l1 and l2:
            res = l1.val + l2.val + carry
            carry = 1 if res > 9 else 0
            curr.next = ListNode(val=res % 10)
            l1, l2, curr = l1.next, l2.next, curr.next

        ll = l1 or l2
        while ll:
            res = ll.val + carry
            carry = 1 if res > 9 else 0
            curr.next = ListNode(val=res % 10)
            ll, curr = ll.next, curr.next

        if carry:
            curr.next = ListNode(val=1)

        return dummy.next