import heapq
from collections import deque, Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #we must always choose the most frequent task first 
        m = len(tasks)
        cpu_freq = Counter(tasks)

        heap = list(cpu_freq.values())
        heapq.heapify_max(heap)

        q = deque()
        cycles = 0

        while heap or q:
            cycles += 1

            if heap:
                count = heapq.heappop_max(heap)
                count -= 1

                if count > 0:
                    q.append((count, cycles + n))
            if q and q[0][1] <= cycles:
                count, _ = q.popleft()
                heapq.heappush_max(heap, count)
        return cycles 


