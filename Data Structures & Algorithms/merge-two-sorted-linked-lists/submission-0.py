# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prev = start = ListNode(val=math.inf)
        c1, c2 = list1, list2
        while c1 and c2:
            if c1.val < c2.val:
                prev.next = c1
                c1 = c1.next
            else:
                prev.next = c2
                c2 = c2.next
            prev = prev.next

        if c1:
            prev.next = c1
        elif c2:
            prev.next = c2

        return start.next