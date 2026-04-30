class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # split nums into k -> non empty subarrays
        # we have to keep the order of the subarray 
        # can be very large subarray 
        # largest sum of subarray is min
        # we can use prefix sum first potentially? 
        l = max(nums) #min value if k was 1
        r = sum(nums)# max sum array if k was 21

        def can(largest):
            subarrays = 1
            current_sum = 0 
            for num in nums:
                if current_sum + num <= largest:
                    current_sum += num
                else:
                    subarrays += 1
                    current_sum = num
            return subarrays <= k

        while l < r:
            mid = (l + r ) // 2

            if can(mid):
                r = mid
            else:
                l = mid + 1

        return l


        