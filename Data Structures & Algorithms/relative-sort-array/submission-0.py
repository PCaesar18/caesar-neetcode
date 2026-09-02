class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hashMap = {val: i for i, val in enumerate(arr2)}

        arr1.sort(key = lambda x: (0, hashMap[x]) if x in hashMap else (1,x))

        return arr1
                
        