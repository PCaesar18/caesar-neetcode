class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        tokens = path.split("/")
        for tok in tokens:
            match tok:
                case "" | ".":
                    pass

                case "..":
                    if stack:
                        stack.pop()

                case _:
                    stack.append(tok)
        return "/" + "/".join(stack)

        