class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_occ = {}
        for num in nums:
            if num in num_occ:
                return True
            else:
                num_occ[num] = 1
        return False
        