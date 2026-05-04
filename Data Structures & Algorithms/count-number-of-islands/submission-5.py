class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        n_islands = 0
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        def islands(r,c):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS) or grid[r][c] == "0":
                return
            grid[r][c] = "0"

            for dr, dc in directions:
                islands(r + dr, c + dc)
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    islands(r,c)
                    n_islands += 1
        return n_islands 
        