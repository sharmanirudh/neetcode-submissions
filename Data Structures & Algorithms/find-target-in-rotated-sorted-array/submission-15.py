class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        if len(nums) == 2:
            if nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            else:
                return -1

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[l] <= nums[mid]: # left half sorted
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                    if r < 0:
                        break
                else:
                    l = mid + 1
                    if l > len(nums) - 1:
                        break
            else: # right half sorted
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                    if l > len(nums) - 1:
                        break
                else:
                    r = mid - 1
                    if r < 0:
                        break

        return -1
