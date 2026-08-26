class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        left_max = height[l]
        right_max = height[r]

        max_area = 0

        while l <= r:
            if height[l] < height[r]:
                left_max = max(height[l], left_max)
                area = left_max - height[l]
                l += 1
            else:
                right_max = max(height[r], right_max)
                area = right_max - height[r]
                r -= 1
            max_area += area if area > 0 else 0

        return max_area
