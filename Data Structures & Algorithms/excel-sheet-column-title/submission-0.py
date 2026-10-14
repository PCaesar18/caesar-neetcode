class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        n = columnNumber

        while n > 0:
            n -= 1
            offset = n % 26
            result += chr(ord('A') + offset)
            n //= 26
        return ''.join(reversed(result))
        