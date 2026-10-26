class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_1 = {}
        map_2 = {}

        for char1, char2 in zip(s,t):
            if char1 in map_1 and map_1[char1] != char2:
                return False
            if char2 in map_2 and map_2[char2] != char1:
                return False
            
            map_1[char1] = char2
            map_2[char2] = char1
        return True


