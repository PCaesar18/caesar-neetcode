import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        "create a priority list based on: shortest processing time, then smallest index "
        " we first handle quickest enque time, and then do the one wirht the quickest processing time"
        "we need the original indexes still there"
        tasks = sorted((enqeue, processing, i) for i, (enqeue, processing) in enumerate(tasks))
        result = []
        pq = []
        i = time = 0

        while pq or i < len(tasks):

            #jump forward if CPU is idle
            if not pq and time < tasks[i][0]:
                time = tasks[i][0]


            while i < len(tasks) and tasks[i][0] <= time:
                enq, process, index = tasks[i]
                heapq.heappush(pq,(process, index))
                i += 1
            processing, index = heapq.heappop(pq)
            time += processing
            result.append(index)
        return result 
        