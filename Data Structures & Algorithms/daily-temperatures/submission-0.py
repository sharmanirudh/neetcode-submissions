class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        result = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack:
                top_t, top_i = stack[-1]
                if t > top_t:
                    stack.pop()
                    result[top_i] = i - top_i
                else:
                    break
            stack.append((t, i))

        return result
