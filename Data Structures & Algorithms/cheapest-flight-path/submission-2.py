class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for source, target, price in flights:
            graph[source].append((target,price))

        
        heap = [(0,src,0)]
        best = {}

        while heap: 
            cost, node, stops = heapq.heappop(heap)

            if node == dst and stops <= k + 1:
                return cost

            if stops > k:
                continue

            if node in best and best[node] <= stops:
                continue
            best[node] = stops

            for nbr, p in graph[node]:
                new_cost = cost + p
                heapq.heappush(heap, (new_cost,nbr,stops + 1))
        return -1 