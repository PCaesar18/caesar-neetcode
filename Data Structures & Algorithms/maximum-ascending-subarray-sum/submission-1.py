class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        result = 0 
        for i in range(len(nums)):
            curSum = nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] <= nums[j - 1]:
                    break
                curSum += nums[j]
            result = max(result, curSum)
        return result 

        