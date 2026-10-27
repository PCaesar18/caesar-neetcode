class Solution:
    def arraySign(self, nums: List[int]) -> int:

        def signFunc(x):
            if x > 0:
                return 1
            elif x < 0:
                return -1
            else:
                return 0
        product = 1
        for num in nums:
            product *= num
        return signFunc(product)
        