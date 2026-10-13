class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for word in words:
            if pref in word and pref == word[:len(pref)]:
                count += 1
        return count 

         #if len(pref) <= len(w) and w[:len(pref)] == pref:

        