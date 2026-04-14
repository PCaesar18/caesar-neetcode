class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #s1 permutation of s2
        # make a window of len s1
        # if counter len(s1) == counter s2 then we return true
        # else we return false
        window_size = len(s1)
        window = Counter(s2[:window_size])
        check = Counter(s1)
        if window == check:
            return True
        l = 0
        for char in range(window_size, len(s2)):
            window[s2[char]] = window.get(s2[char],0) + 1
            window[s2[l]] -= 1
            if window[s2[l]] == 0:
                del window[s2[l]]
            l += 1

            if window == check:
                return True
        return False 

        