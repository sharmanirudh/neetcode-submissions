class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)

        l, r = 0, len(A) - 1
        total = len(A) + len(B)
        half = total // 2

        while True:
            i = (l + r) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else -math.inf
            Aright = A[i + 1] if i + 1 < len(A) else math.inf
            Bleft = B[j] if j >=0 else -math.inf
            Bright = B[j + 1] if j + 1 < len(B) else math.inf

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
