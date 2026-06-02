class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        

        while top <= bot:
            rows = (top + bot) // 2
            if matrix[rows][-1] < target:
                top = rows +1
            elif matrix[rows][0] > target:
                bot = rows - 1
            else:
                break

        rows = (top + bot) // 2
        l, r = 0, COLS - 1

        while l <= r:
            mid = (l+r) // 2
            if matrix[rows][mid] < target:
                l = mid + 1
            elif matrix[rows][mid] > target:
                r = mid -1
            else:
                return True
        return False