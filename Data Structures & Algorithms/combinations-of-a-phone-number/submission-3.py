class Solution:
    def letterCombinations(self, digits: str) -> List[str]:        
        result = []
        translate = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, path):
            if i == len(digits):
                result.append(path)
                return
            
            for char in translate[digits[i]]:
                backtrack(i + 1, path + char)
        if digits:
            backtrack(0, "")

        return result

        