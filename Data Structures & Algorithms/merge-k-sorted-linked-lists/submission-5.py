# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        start = curr = ListNode()
        
        heads = [(n.val, i) for i, n in enumerate(lists) if n]
        heapq.heapify(heads)

        while heads:
            (val, idx) = heapq.heappop(heads)
            curr.next = lists[idx]
            curr = curr.next
            if lists[idx].next:
                lists[idx] = lists[idx].next
                heapq.heappush(heads, (lists[idx].val, idx))

        return start.next
        