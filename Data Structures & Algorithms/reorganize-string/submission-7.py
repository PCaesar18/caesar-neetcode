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

            if prev_freq > 0: #temp keep prev char out of heap
                heapq.heappush_max(pq,(prev_freq, prev_char))
            
            prev_freq, prev_char = freq, char
        return "".join(result)

        #time complexity = NlogK (n = total num of chars, k = unique chars)

        #When you have a heap inside a loop, separate the two questions:
#1. How many times does the loop run? → O(N)
#2. How expensive is each heap operation? → O(log K)
        # space complexity = On
        #Space complexity
#Heap: O(K)
#- Counter: O(K)
#- Result: O(N)
#Total space: O(N + K) = O(N) because K ≤ N.

        