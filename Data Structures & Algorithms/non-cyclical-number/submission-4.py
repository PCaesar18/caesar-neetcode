class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False
            seen.add(n)

            squares = 0

            while n > 0:
                digit = n % 10
                squares += digit ** 2
                n //= 10
            n = squares
        return True

    






        