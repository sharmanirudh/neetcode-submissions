class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_chars = {}
        for c in t:
            t_chars[c] = t_chars.get(c, 0) + 1

        present_count = 0
        result = ""
        l = 0
        r = -1
        window_chars = {}
        while l < len(s) and r < len(s):
            if present_count < len(t):
                r += 1
                if r == len(s):
                    break
                c = s[r]
                window_chars[c] = window_chars.get(c, 0) + 1
                if c in t and window_chars[c] <= t_chars[c]:
                    present_count += 1

            elif present_count == len(t):
                c = s[l]
                window_chars[c] = window_chars[c] - 1
                if c in t and window_chars[c] < t_chars[c]:
                    present_count -= 1
                l += 1

            if present_count == len(t) and (not result or r - l + 1 <= len(result)):
                    result = s[l:r+1]

        return result