class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = slow = fast = 0

        while i == 0 or slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
            i += 1

        slow2 = 0
        while slow != slow2:
            slow2 = nums[slow2]
            slow = nums[slow]

        return slow2
