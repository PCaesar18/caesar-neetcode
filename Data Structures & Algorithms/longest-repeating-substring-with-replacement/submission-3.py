class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #window_size - max_frequency ≤ k
        freq_count = {}
        l = 0
        maxFreq = 0
        result = 0 
        for r in range(len(s)):
            freq_count[s[r]] = freq_count.get(s[r], 0) + 1
            maxFreq = max(maxFreq, freq_count[s[r]])
            
            while (r - l + 1) - maxFreq > k: 
                freq_count[s[l]] -= 1
                l += 1
        result = max(result, r - l + 1)
        return result 
        