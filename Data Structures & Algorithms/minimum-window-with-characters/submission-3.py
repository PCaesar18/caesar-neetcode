class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result = ""
        if len(s) < len(t):
            return result 

        best_len = float('inf')
        l = 0

        tmap = Counter(t)
        window = Counter()

        have = 0 #Number of characters that currently meet required frequency
        need = len(tmap) #Total number of distinct characters we need to satisfy

        for r in range(len(s)):
            window[s[r]] += 1

            if s[r] in tmap and window[s[r]] == tmap[s[r]]:
                have += 1
                # here we check if window is valid 
            while have == need:
                # Try to update the best (smallest) window
                if r - l + 1 < best_len:
                    best_len = r - l + 1
                    result = s[l:r + 1]
                window[s[l]] -= 1
                #if after removing left most char breaks the window then window is no longer valid 
                if s[l] in tmap and window[s[l]] < tmap[s[l]]:
                    have -= 1
                l += 1
        return result 




        #work on new orgs 
        # apply for jobs
        # more programming 
        #training
        # meet Pep this week
        # chillz with alfi & dide 
        