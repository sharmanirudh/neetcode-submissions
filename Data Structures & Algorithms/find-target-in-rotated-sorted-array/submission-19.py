class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[l] <= nums[mid]:
                # mid belongs to the left-half sorted
                if nums[l] <= target < nums[mid]:
                    # mid lies b/w the range of left sorted half
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                # mid belongs to the right-half sorted
                if nums[mid] < target <= nums[r]:
                    # mid lies b/w the range of right sorted half
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
