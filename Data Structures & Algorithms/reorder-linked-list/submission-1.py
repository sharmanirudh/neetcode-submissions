# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = slow
        curr = slow.next
        slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        n = head
        while n:
            print(n.val, end=", ")
            n = n.next
        print()
        n = prev
        while n:
            print(n.val, end=", ")
            n = n.next

        l = head
        r = prev
        while r and l:
            temp1, temp2 = l.next, r.next
            l.next = r
            if r != temp1:
                r.next = temp1
            l = temp1
            r = temp2
