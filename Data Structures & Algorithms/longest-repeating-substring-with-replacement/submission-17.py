class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxf = 0
        l, r = 0, 0
        counts = {}
        topc = s[r]

        while r < len(s):
            counts[s[r]] = counts.get(s[r], 0) + 1

            if counts[topc] < counts[s[r]]:
                topc = s[r]

            if r - l + 1 - counts[topc] <= k:
                maxf = max(maxf, r - l + 1)
            else:
                counts[s[l]] -= 1
                topc = max((c, ch) for ch, c in counts.items())[1]
                l += 1

            r += 1
        
        return maxf
