class Solution:
    def isValid(self, s: str) -> bool:
        stack = collections.deque()
        bracket_map = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        for c in s:
            if c in bracket_map:
                if not stack:
                    return False
                elif stack[-1] != bracket_map[c]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)

        if not stack:
            return True
        else:
            return False