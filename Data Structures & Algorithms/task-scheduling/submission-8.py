import heapq
from collections import deque, Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = list(count.values())
        heapq.heapify_max(heap)
        q = deque() #time, count
        time = 0

        while q or heap:
            time += 1

            if heap:
                cnt = heapq.heappop_max(heap)
                cnt -= 1

                if cnt > 0:
                    q.append((time + n, cnt))

            if q and q[0][0] <= time:
                _, cnt = q.popleft()
                heapq.heappush_max(heap, cnt)
        return time