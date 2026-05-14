class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_string = ""
        curr_num = 0

        for char in s: 
            match char:
                case c if c.isdigit():
                    curr_num = curr_num * 10 + int(c)

                case "[":
                    stack.append((curr_string, curr_num))
                    curr_string = ""
                    curr_num = 0

                case "]":
                    string, num = stack.pop()
                    curr_string = string + curr_string * num
                
                case c:
                    curr_string += c
        return curr_string


        