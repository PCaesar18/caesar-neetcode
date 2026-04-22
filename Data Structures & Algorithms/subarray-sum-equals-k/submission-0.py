class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = defaultdict(int)
        result = 0
        curr = 0

        for num in nums:
            hashmap[curr] += 1
            curr += num
            result += hashmap[curr - k]
        return result 
