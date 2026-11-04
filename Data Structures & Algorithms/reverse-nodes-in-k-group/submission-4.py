# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseLL(self, start, end):
        prev, curr = None, start
        stop_at = end.next
        while curr != stop_at:
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        new_head = None
        prev_tail = None
        left = right = head
        pos = 1
        while right:
            if pos == k:
                new_head = right
            if pos % k == 0:
                next_start = right.next
                self.reverseLL(left, right)
                if prev_tail:
                    prev_tail.next = right
                prev_tail = left
                print(left.val)
                left.next = next_start
                left, right = right, left
            if pos >= k:
                left = left.next
            right = right.next
            pos += 1

        return new_head