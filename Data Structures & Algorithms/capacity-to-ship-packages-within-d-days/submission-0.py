class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #binary search on answer
        # the range is from max weight array to somewhere higher 

        # we trying find min possible answer
        #range is from max(weight) to 
        # answer has to fit within number of days 
        l = max(weights)
        r = sum(weights) # if we have to load everything in 1 day

        #monotonic helper function
        # we have to go through the weights in order 

        def can(cap):
            current_load = 0
            days_used = 1 # we always start shipping on day 1
            for weight in weights:
                if (current_load + weight) <= cap:
                    current_load += weight
                else:
                    days_used += 1
                    current_load = weight
                if days_used > days:
                    return False
            return True if days_used <= days else False

        while l < r:
            mid = (l + r) // 2

            if can(mid):
                r = mid
            else:
                l = mid + 1
        return l

                


        