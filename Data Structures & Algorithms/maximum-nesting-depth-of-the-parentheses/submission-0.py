class Solution:
    def maxDepth(self, s: str) -> int:

        stack = []
        result = 0

        for char in s:
            if char == "(":
                stack.append(char)
                
            elif stack and char == ")":
                stack.pop()
                
            result = max(result, len(stack))
        return result 

        