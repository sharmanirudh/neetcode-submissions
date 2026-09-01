class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        result = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                top_t, top_i = stack[-1]
                stack.pop()
                result[top_i] = i - top_i
            stack.append((t, i))

        return result
