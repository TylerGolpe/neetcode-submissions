class Solution:
    def isValid(self, s: str) -> bool:
        values = {")" : "(", "]" : "[", "}" : "{"}
        stack = []
        for char in s:
            if char in values:
                if not stack or stack.pop() != values[char]:
                    return False
            else:
                stack.append(char)

        return not stack
                
