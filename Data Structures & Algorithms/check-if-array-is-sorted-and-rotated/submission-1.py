class Solution:
    def check(self, nums: List[int]) -> bool:
        #if there is more than one pivot, there is a false

        pivot = 0 
        n = len(nums)
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                pivot += 1
        return True if pivot <= 1 else False 
        