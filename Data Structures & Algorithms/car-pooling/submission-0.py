class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        prefix = [0] * 1001
        for passengers, start, end in trips:
            prefix[start] += passengers
            prefix[end] -= passengers

        current = 0

        for pref in prefix:
            current += pref

            if current > capacity:
                return False
        return True             