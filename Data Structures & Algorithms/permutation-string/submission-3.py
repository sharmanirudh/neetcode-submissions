class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_counts_1 = {}
        for ch in s1:
            char_counts_1[ch] = char_counts_1.get(ch, 0) + 1

        res = False

        for l in range(len(s2) - len(s1) + 1):
            char_counts_2 = {}
            for r in range(l, l + len(s1)):
                ch = s2[r]
                char_counts_2[ch] = char_counts_2.get(ch, 0) + 1
                if ch not in char_counts_1 or char_counts_2[ch] > char_counts_1[ch]:
                    res = False
                    break
            if char_counts_2 == char_counts_1:
                res = True
                break

        return res
