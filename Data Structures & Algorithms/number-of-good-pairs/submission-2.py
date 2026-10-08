class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        seen = {}
        count = 0

        for num in nums:
            if num in seen:
                count += seen[num]
            seen[num] = seen.get(num, 0) + 1

        return count 
            

        

        