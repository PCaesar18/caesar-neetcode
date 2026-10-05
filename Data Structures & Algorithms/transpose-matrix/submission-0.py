class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(matrix), len(matrix[0])
        temp = [[0] * ROWS for _ in range(COLS)]

        for r in range(ROWS):
            for c in range(COLS):
                temp[c][r] = matrix[r][c]

        return temp
        