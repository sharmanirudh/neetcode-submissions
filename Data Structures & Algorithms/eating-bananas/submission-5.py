class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = piles[0]
        for p in piles:
            max_pile = max(p, max_pile)

        k = max_pile
        l, r = 1, max_pile
        while l <= r:
            kk = l + (r - l) // 2
            hh = 0
            for i, p in enumerate(piles):
                hh += math.ceil(p / kk)
                if hh > h:
                    break
            if hh > h:
                l = kk + 1
            else:
                r = kk - 1
                k = min(kk, k)
            # else:
            #     k = min(kk, k)

        return k