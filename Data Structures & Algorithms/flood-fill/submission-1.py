class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(1,0),(0,1),(0,-1),(-1,0)]
        ROWS, COLS = len(image), len(image[0])
        original = image[sr][sc]
        if original == color:
            return image



        def dfs(r, c):
            if r <0 or r >= ROWS or c < 0 or c >= COLS or image[r][c] != original:
                return
            

            image[r][c] = color
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                dfs(nr,nc)
        dfs(sr,sc)
        return image 





    #         class Solution:
    # def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    #     start_color = image[sr][sc]
    #     if start_color == color:
    #         return image
    #     def dfs(i, j):
    #         if not 0 <= i < len(image) or not 0 <= j < len(image[0]):
    #             return
    #         if image[i][j] != start_color:
    #             return
            
    #         image[i][j] = color
    #         dfs(i + 1, j)
    #         dfs(i - 1, j)
    #         dfs(i, j + 1)
    #         dfs(i, j - 1)
    #     dfs(sr, sc)
    #     return image


        