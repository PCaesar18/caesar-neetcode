class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l, r = 0, sum(nums)
        for i, val in enumerate(nums):
            r -= val
            if l == r:
                return i
            l += val
        return -1