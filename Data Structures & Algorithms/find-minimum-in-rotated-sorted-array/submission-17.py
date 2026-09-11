class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        min_num = nums[0]

        while l <= r:
            mid = l + (r - l) // 2
            if nums[l] <= nums[mid]:
                min_num = min(nums[l], min_num)
                l = mid + 1
            else:
                min_num = min(nums[mid], min_num)
                r = mid - 1

        return min_num
