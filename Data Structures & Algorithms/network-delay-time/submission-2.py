class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v,t))

        
        heap = [(0,k)]
        distance = {}

        while heap:
            time, node = heapq.heappop(heap)

            if node in distance:
                continue
            distance[node] = time

            for nbr, t in adj[node]:
                new_time = time + t
                if nbr not in distance:
                    heapq.heappush(heap, (new_time, nbr))

        if len(distance) != n:
            return -1
        return max(distance.values())

        