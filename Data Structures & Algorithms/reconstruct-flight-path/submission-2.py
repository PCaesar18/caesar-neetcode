class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        for source, destination in tickets:
            heapq.heappush(adj[source], destination)

        result = []

        def dfs(node):
            while adj[node]:
                nxt = heapq.heappop(adj[node])
                dfs(nxt)
            result.append(node)



        dfs("JFK")
        return result[::-1]






        