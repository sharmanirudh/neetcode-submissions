class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        i = 0
        while i < len(nums) and nums[i] <= 0:
            a = nums[i]
            if i > 0 and a == nums[i - 1]:
                i += 1
                continue
            target = -1 * a
            j, k = i + 1, len(nums) - 1
            while j < k:
                b, c = nums[j], nums[k]
                if b + c < target:
                    j += 1
                elif b + c > target:
                    k -= 1
                else:
                    triplets.append((a, b, c))
                    j += 1
                    k -= 1
                while i + 1 < j < k and nums[j] == nums[j - 1]:
                    j += 1
                while j < k < len(nums) - 1 and nums[k] == nums[k + 1]:
                    k -= 1
            i += 1

        return triplets