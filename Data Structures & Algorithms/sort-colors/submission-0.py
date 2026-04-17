class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        #dutch flag solution with 3 colors 
        """
        # my two thoughts are either 1) loop through the array, sent all encountering 0's all the way to the front, and all the two's all the way to the back of the array.
        # other option is two pointers where we loop through the array 
        left = 0
        right = len(nums) - 1
        i = 0
        while i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
                


        