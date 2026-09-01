class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                (prev_i, prev_h) = stack.pop()
                area = (i - prev_i) * prev_h
                max_area = max(area, max_area)
                start = prev_i
            stack.append((start, h))

        i = len(heights)
        while stack:
            (prev_i, prev_h) = stack.pop()
            area = (i - prev_i) * prev_h
            max_area = max(area, max_area)

        return max_area