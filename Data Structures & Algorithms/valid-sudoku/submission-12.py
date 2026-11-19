class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for r in range(9):
            row_counts = {}
            col_counts = {}
            for c in range(9):
                # check duplicate in row
                num = board[r][c]
                if num in row_counts and num != ".":
                    return False
                else:
                    row_counts[num] = 1
                # check duplicate in column
                num = board[c][r]
                if num in col_counts and num != ".":
                    return False
                else:
                    col_counts[num] = 1

        for i in (0, 3, 6):
            for j in (0, 3, 6):
                box_counts = {}
                for r in range(i, i+3):
                    for c in range(j, j+3):
                        num = board[r][c]
                        if num in box_counts and num != ".":
                            return False
                        else:
                            box_counts[num] = 1
        return True
        