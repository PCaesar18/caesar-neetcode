class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = ""
        first = strs[0]

        for char in range(len(first)):
            for string in strs:
                if char == len(string) or string[char] != first[char]:
                    return string[:char]
        return first


        