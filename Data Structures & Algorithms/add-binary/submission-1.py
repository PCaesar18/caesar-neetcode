class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = "0"
        for aa, bb in zip_longest(reversed(a), reversed(b), fillvalue = "0"):
            if aa == bb:
                result.append(carry)
                carry = aa
            else:
                result.append("1" if carry == "0" else "0")
        if carry == "1":
            result.append("1")
        return "".join(reversed(result))
        