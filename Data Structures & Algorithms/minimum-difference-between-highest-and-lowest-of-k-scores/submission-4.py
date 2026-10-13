class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        left = 0
        res = float("inf")

        for r in range(k -1, len(nums)):
            res = min(res, nums[r] - nums[left])
            left += 1
        return res
        