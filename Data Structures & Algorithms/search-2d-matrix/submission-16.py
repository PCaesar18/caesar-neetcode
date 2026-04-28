class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # we can use binary search
        # we can check first value in each row. against the target, if we have found the row -> we can binary search in the row
        ROWS = len(matrix)
        COLS = len(matrix[0])

        
        l, r = 0, ROWS * COLS -1
        while l <= r:
            mid = (l + r ) // 2
            row = mid // COLS
            col = mid % COLS
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
        