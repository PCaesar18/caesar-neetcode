from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cpu = Counter(tasks)
        max_heap = list(cpu.values())
        heapq.heapify_max(max_heap)
        time = 0

        q = deque() #time, count
        while max_heap or q:
            time += 1

            while q and q[0][0] <= time:
                ready, count = q.popleft()
                heapq.heappush_max(max_heap, count)

            if max_heap:
                count = heapq.heappop_max(max_heap)
                count -= 1

                if count > 0:
                    q.append((time + n + 1,count))
        return time 
        