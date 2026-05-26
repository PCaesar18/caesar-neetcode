class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # lets try it with dp

        #first try 2 pointers

        l, r = 0 , 0 
        while l < len(s) and r < len(t):
            if s[l] == t[r]:
                l += 1
                r += 1
            else:
                r += 1
        return l == len(s)



        