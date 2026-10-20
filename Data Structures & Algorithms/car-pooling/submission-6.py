import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: x[1])
        heap = []
        current = 0
        for pas, src, dest in trips:
            while heap and heap[0][0] <= src:
                dropoff, count = heapq.heappop(heap)
                current -= count
            
            current += pas

            if current > capacity:
                return False
            heapq.heappush(heap, (dest, pas))
        return True

        