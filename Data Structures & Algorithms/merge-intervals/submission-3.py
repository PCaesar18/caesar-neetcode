class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        merged = [intervals[0]]

        for start, end in intervals:
            last = merged[-1][1]
            if start > last:
                merged.append([start,end])
            else:
                merged[-1][1] = max(last, end)
        return merged 


            
        