class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxheap = [] # we should push a priority/l value, we drop the lowest l every time we move right
        result = []
        l = 0
        for r in range(len(nums)): 
            heapq.heappush_max(maxheap, (nums[r], r))

             #remove elements outside the window
            while maxheap[0][1] < l:
                heapq.heappop_max(maxheap)

            if r - l + 1 ==k:
                result.append(maxheap[0][0])
                l += 1


        return result 


        