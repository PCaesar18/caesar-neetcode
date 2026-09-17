class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = [[x**2 + y**2, [x,y]] for x, y in points]
        result = []
        heapq.heapify(minheap)
        while k > 0:
            result.append(heapq.heappop(minheap)[1])
            k -= 1
        return result 




        