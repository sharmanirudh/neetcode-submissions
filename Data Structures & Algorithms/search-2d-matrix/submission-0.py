class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nrows = len(matrix)
        ncols = len(matrix[0])
        n = nrows * ncols
        l, r = 0, n-1
        while l <= r:
            mid = l + (r - l) // 2
            i = mid // ncols
            j = mid % ncols
            if matrix[i][j] == target:
                return True
            elif  matrix[i][j] <= target:
                l = mid + 1
            else:
                r = mid - 1

        return False
