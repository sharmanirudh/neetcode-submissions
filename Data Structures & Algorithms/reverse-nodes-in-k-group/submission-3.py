# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        p1 = p2 = head
        prev_tail = None
        pos = 1
        while p1:
            if pos % k == 0:
                new_head = p1
                p1 = self.reverseLL(p2, p1.next)
                if prev_tail:
                    prev_tail.next = new_head
                else:
                    head = new_head
                p2.next = p1
                prev_tail = p2
                p2 = p1
                pos += 1
            else:
                p1 = p1.next
                pos += 1

        return head
    
    def reverseLL(self, start, end):
        prev, curr = None, start
        while curr != end:
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp
        return end