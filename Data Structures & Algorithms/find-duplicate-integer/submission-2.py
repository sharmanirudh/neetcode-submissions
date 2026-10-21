class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        for _ in nums:
            slow = nums[slow] 
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        for _ in nums:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow2 == slow:
                return slow

        return None