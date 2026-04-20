from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for source, target, time in times:
            graph[source].append((target,time))

        heap = [(0,k)] #k is the starting node
        distance = {} #allows us to track information and visited nodes

        while heap:
            time, node = heapq.heappop(heap) # we need to sort our heap based on the time (t)

            if node in distance:
                continue #or skip
            distance[node] = time

            for nbr, t in graph[node]:
                new_time = time + t
                if nbr not in distance:
                    heapq.heappush(heap,(new_time,nbr))
        if len(distance) != n:
            return -1
        return max(distance.values())
        