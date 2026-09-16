class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        left = 0

        for char in s:
            if left < len(t) and t[left] == char:
                left += 1
        return len(t) - left 

            
        