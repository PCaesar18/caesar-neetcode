class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        result = nums[0]
        sub_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= nums[i -1]:
                sub_sum = 0
            sub_sum += nums[i]
            result = max(result, sub_sum)
        return result 


        