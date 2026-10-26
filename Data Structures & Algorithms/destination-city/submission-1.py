class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        visited = set()

        for src, _ in paths:
            visited.add(src)

        for _, dst in paths:
            if dst not in visited:
                return dst
