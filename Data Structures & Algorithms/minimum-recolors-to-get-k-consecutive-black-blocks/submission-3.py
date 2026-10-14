class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_ops = float("inf")
        l = 0

        for r in range(k, len(blocks)+ 1):
            recolor = blocks[l:r].count('W')
            min_ops = min(min_ops, recolor)
            l += 1
        return min_ops

        
        