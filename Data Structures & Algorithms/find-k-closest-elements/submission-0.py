class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # we find the target element and then grow the window in both directions
        def findK(index):
            return x - arr[index] <= arr[index + k] - x 

        l, r = 0, len(arr) - k 

        while l < r:
            mid = (l + r) // 2
            if findK(mid):
                r = mid
            else:
                l = mid + 1
        return arr[l:l + k]

        