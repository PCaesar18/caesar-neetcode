import heapq
from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        #if one is more than half of the total, then it would not be possible to split them up 
        "Your intuition is spot on: if any character's frequency exceeds (len(s) + 1) // 2, it is impossible to rearrange without adjacent duplicates. Now, think about which characters you should place first to avoid running into conflicts later."
        " we should place most frequent characters first/greedy strategy for placement "
        count = Counter(s)
        heap = [(freq,char) for char, freq in count.items()]
        heapq.heapify_max(heap)
        result = ""
        n = len(s)
        if count.most_common(1)[0][1] > (n + 1) >> 1:
            return ""
        
        prev_freq, prev_char = 0, ""
        while heap:
            freq,char = heapq.heappop_max(heap) 

            result += char
            freq -= 1
            if prev_freq > 0:
                heapq.heappush_max(heap, (prev_freq, prev_char))
            
            prev_freq, prev_char = freq, char
        return result


        