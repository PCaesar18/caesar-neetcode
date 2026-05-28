class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # we have to both track the max and the min
        result = nums[0]
        curmin, curmax = 1,1

        for num in nums:
            tmp = curmax * num
            curmax = max(num, curmax * num, curmin * num)
            curmin = min(tmp, curmin * num, num)
            result = max(result, curmax)
        return result 
        