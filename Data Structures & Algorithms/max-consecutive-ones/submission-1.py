class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        total = 0
        running = 0

        for num in nums:
            if num & 1:
                running += 1
                total = max(total, running)
            else:
                running = 0
        return total
        