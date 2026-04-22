class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #have to return integer, not list per se
        # what is the fastest option? multiple pointers, hash set? to filter out a spefic value in an array? 
        k = 0
        for i in range(len(nums)):
            if nums[i] != val: #we walk over while we do not see the value, if we do, we skip over it
                nums[k] = nums[i]
                k += 1
        return k 


        