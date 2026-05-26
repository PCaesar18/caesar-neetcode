class Solution:
    def tribonacci(self, n: int) -> int:
        first, second , third = 0, 1, 1

        for i in range(n):
            first, second, third = second, third, first + second + third
        return first
        