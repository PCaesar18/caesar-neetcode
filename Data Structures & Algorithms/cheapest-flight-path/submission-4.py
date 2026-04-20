class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #lets try bellman ford
        prices = [float("inf")] * n
        prices[src] = 0

        for _ in range(k + 1):
            temp = prices.copy()

            for source, dest, cost in flights:
                if prices[source] == float('inf'):
                    continue
                temp[dest] = min(temp[dest], prices[source] + cost)
            prices = temp
        
        return -1 if prices[dst] == float('inf') else prices[dst]












        # graph = defaultdict(list)
        # for source, target, price in flights:
        #     graph[source].append((target,price))

        
        # heap = [(0,src,0)]
        # best = {}

        # while heap: 
        #     cost, node, stops = heapq.heappop(heap)

        #     if node == dst and stops <= k + 1:
        #         return cost

        #     if stops > k:
        #         continue

        #     if node in best and best[node] <= stops:
        #         continue
        #     best[node] = stops

        #     for nbr, p in graph[node]:
        #         new_cost = cost + p
        #         heapq.heappush(heap, (new_cost,nbr,stops + 1))
        # return -1 