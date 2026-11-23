class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        #priority queue of min processing time, smallest index (probably min heap)
        tasks = [(start, duration, i) for i, (start, duration) in enumerate(tasks)]
        tasks.sort(key = lambda task: task[0])

        heap = []
        time = 0
        index = 0
        result = []

        while index < len(tasks) or heap: 

            if not heap and time < tasks[index][0]: #basically we skip forward till we get the first task
                time = tasks[index][0]

            while index < len(tasks) and tasks[index][0] <= time:
                start, duration, i = tasks[index]
                heapq.heappush(heap, (duration, i))

                index += 1
            
            duration, i = heapq.heappop(heap)
            time += duration
            result.append(i)

        return result 