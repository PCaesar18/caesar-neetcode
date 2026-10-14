from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)
        heap = list(count.values())
        heapq.heapify_max(heap)
        time = 0

        q = deque() #time, count

        while q or heap:
            time += 1
            while q and q[0][0] <= time:
                new_time, count = q.popleft()
                heapq.heappush_max(heap, count)
            if heap:
                count = heapq.heappop_max(heap)
                count -= 1
                
                if count > 0:
                    q.append((time + n + 1, count))
        return time    