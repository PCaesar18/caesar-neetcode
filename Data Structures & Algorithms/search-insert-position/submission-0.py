class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #sorted in ascending order
        #large num length
        #binary search
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return l #l is the insertion index because l naturally lands on the correct position


        #built in binary search function
        #return bisect.bisect_left(nums, target) #bisect_right for upper bound


        