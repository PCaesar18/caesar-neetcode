class Solution:
    def check(self, nums: List[int]) -> bool:
        #if there is more than one pivot, there is a false

        pivot = 0 
        for i in range(len(nums)):
            if nums[i] > nums[(i + 1) % len(nums)]:
                pivot += 1
        return True if pivot <= 1 else False 
        