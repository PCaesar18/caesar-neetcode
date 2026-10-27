class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0

        def backtrack(i, current):
            nonlocal total

            if i == len(nums):
                total += current
                return
            backtrack(i + 1, current ^ nums[i])
            backtrack(i + 1, current)
        backtrack(0,0)
        return total 

        