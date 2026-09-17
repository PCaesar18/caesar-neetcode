class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)

        return any(freq > 1 for freq in count.values())
        