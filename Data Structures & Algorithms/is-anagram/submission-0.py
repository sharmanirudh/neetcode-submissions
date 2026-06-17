class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_chars, t_chars = {}, {}
        for idx in range(len(s)):
            if s[idx] in s_chars:
                s_chars[s[idx]] += 1
            else:
                s_chars[s[idx]] = 1
            if t[idx] in t_chars:
                t_chars[t[idx]] += 1
            else:
                t_chars[t[idx]] = 1

        for c, count in s_chars.items():
            if c not in t_chars or t_chars[c] != count:
                return False
        
        return True