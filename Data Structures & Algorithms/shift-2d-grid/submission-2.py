class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        ROWS, COLS = len(grid), len(grid[0])
        if k == 0:
            return grid
        #can put it in a list and then rebuild the original grid again 
        k %= ROWS * COLS

        res = [[0] * COLS for _ in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                new = (r * COLS + c + k) % (ROWS * COLS)
                new_r = new // COLS
                new_c = new % COLS

                res[new_r][new_c] = grid[r][c]
        return res 



        
