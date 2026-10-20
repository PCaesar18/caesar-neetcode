class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_loc = max(dest for _, _, dest in trips)
        changes = [0] * (max_loc + 1)

        for pas, src, dst in trips:
            changes[src] += pas
            changes[dst] -= pas

        current = 0

        for change in changes:
            current += change

            if current > capacity:
                return False
        return True 


        