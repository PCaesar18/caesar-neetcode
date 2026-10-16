class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result = []
        count = Counter({'a': a, 'b': b, 'c': c})

        heap = [(freq, char) for char, freq in count.items() if freq > 0]
        heapq.heapify_max(heap)

        # we can check the tail of the result 
        while heap: 
            freq, char = heapq.heappop_max(heap)


            if len(result) >= 2 and result[-1] == result[-2] == char:
                if not heap:
                    break
                else:
                    next_freq, next_char = heapq.heappop_max(heap)
                    result.append(next_char)
                    next_freq -= 1
                    if next_freq > 0:
                        heapq.heappush_max(heap,(next_freq, next_char))
                    heapq.heappush_max(heap,(freq,char))
            else:
                result.append(char)
                freq -= 1
                if freq > 0:
                    heapq.heappush_max(heap, (freq,char))
        return "".join(result)



        "we can add two but not three of the same"
        