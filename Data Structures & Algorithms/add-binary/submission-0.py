class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        n = len(a) -1
        m = len(b) -1
        result = [] 


        while n >= 0 or m >= 0 or carry:
            total = carry
            if n >= 0:
                total += int(a[n])
                n -= 1
            if m >= 0:
                total += int(b[m])
                m -= 1
            result.append(str(total % 2))
            carry = total // 2
        return "".join(reversed(result))


        
