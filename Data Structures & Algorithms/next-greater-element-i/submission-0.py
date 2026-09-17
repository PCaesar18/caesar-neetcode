class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        greater = {}

        for i, num in enumerate(nums2):
            while stack and stack[-1] < num:
                smaller = stack.pop()
                greater[smaller] = num
            stack.append(num)

        return [greater.get(num, -1) for num in nums1]


        