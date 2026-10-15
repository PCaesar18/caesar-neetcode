class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        n = len(s)
        result = []
        if count.most_common(1)[0][1] > (n + 1) >> 1:
            return ""
        
        heap = [(freq,char) for char, freq in count.items()]
        heapq.heapify_max(heap)

        prev_freq, prev_char = 0, ""

        while heap:
            freq, char = heapq.heappop_max(heap)

            result.append(char)
            freq -= 1

            if prev_freq > 0:
                heapq.heappush_max(heap,(prev_freq, prev_char))
            prev_freq, prev_char = freq, char
        return "".join(result)