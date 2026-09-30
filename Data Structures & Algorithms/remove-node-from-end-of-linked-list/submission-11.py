# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        half = 0
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            half += 1

        if fast:
            size = half * 2 + 1
        else:
            size = half * 2

        pos = size - n + 1
        start, prev, curr = 1, ListNode(), head

        print(f"{size = }, {half = }, {pos = }, {start = }, {prev.val = }, {curr.val = }")

        if pos == 1 and size == 1:
            head = None

        else:
            for i in range(start, pos + 1):
                if i == pos:
                    prev.next = curr.next
                    curr.next = None
                    if pos == 1:
                        head = prev.next
                    break
                prev = curr
                curr = curr.next
        
        return head