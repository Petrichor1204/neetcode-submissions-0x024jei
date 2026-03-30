class Solution:
    def isValid(self, s: str) -> bool:
        closing = {")":"(", "]":"[", "}":"{"}
        paren = "([{"
        stack = []
    
        for char in s:
            if char in paren:
                stack.append(char)
            else:
                if stack and stack[-1] == closing[char]:
                    stack.pop() 
                else:
                    return False
        return not stack

                
                

