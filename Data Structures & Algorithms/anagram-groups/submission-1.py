class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for st in strs:
            key = ''.join(sorted(st))
            result[key].append(st)
        return list(result.values())