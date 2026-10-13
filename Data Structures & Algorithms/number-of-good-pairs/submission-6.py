class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        total = 0

        for num in nums:
            total += seen[num]
            seen[num] += 1
        return total 


        