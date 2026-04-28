class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        l = self.mySqrt(x >> 2) << 1
        r = l + 1
        return l if r ** 2 > x else r
        
        # l, r = 0, x // 2
        # while l <= r:
        #     mid = (l + r) // 2
        #     if mid * mid == x:
        #         return mid
        #     elif mid * mid < x:
        #         l = mid + 1
        #     else:
        #         r = mid - 1
        # return r


        