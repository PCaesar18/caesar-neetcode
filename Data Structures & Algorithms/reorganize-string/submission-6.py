import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        n = len(s)

        if max(count.values()) > (n + 1) >> 1:
            return ""
        
        pq = [(freq, char) for char, freq in count.items()]
        heapq.heapify_max(pq)

        prev_freq, prev_char = 0, ""
        result = []

        while pq:
            freq, char = heapq.heappop_max(pq)
            result.append(char)
            freq -= 1

            if prev_freq > 0:
                heapq.heappush_max(pq,(prev_freq, prev_char))
            
            prev_freq, prev_char = freq, char
        return "".join(result)

        