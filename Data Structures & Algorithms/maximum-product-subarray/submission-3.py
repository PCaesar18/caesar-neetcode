class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # we have to both track the max and the min
        n = len(nums)
        dpmax = [0] * n
        dpmin = [0] * n

        dpmax[0] = nums[0]
        dpmin[0] = nums[0]
        result = nums[0]
        for i in range(1, n):
            num = nums[i]
            dpmax[i] = max(num, num * dpmax[i-1], num * dpmin[i-1])
            dpmin[i] = min(num, num * dpmax[i-1], num * dpmin[i-1])
            result = max(result,dpmax[i])
        return result 

        