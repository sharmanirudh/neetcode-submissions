class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        min_num = nums[0]

        while l <= r:
            mid = l + (r - l) // 2
            if nums[l] > nums[mid]:
                r = mid - 1
                if r < 0:
                    break
                min_num = min(nums[mid], min_num)
            else:
                l = mid + 1
                if l > len(nums) - 1:
                    break
                min_num = min(nums[mid], nums[l], min_num)
        return min_num