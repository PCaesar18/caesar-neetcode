class Solution:
    def specialArray(self, nums: List[int]) -> int:
        l,r = 0, len(nums)
        while l <= r:
            mid = (l + r) // 2

            count = sum(1 for num in nums if num >= mid)

            if count == mid:
                return mid
            if count < mid:
                r = mid - 1
            else:
                l = mid + 1
        return - 1