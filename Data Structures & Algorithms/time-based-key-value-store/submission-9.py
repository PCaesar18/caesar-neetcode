class TimeMap:

    def __init__(self):
        #we can make a hashmap storing a tuple
        # when setting and getting, we can use binary search to find for the given timestamp 
        self.store = defaultdict(list)  # key -> list of (timestamp, value)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        arr = self.store[key]
        l, r = 0, len(arr) - 1
        result = ""
        while l <= r:
            mid = (l + r) // 2
            if arr[mid][0] <= timestamp:
                l = mid + 1
                result = arr[mid][1]
            else:
                r = mid - 1
        return result 

        #return most recent value of key
        
