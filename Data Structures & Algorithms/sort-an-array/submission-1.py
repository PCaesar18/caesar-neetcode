class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        middle = n //2
        if n <= 1:
            return nums
        left = self.sortArray(nums[:middle])
        right = self.sortArray(nums[middle:])

        return self.merge(left, right)
    def merge(self, left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result 
        