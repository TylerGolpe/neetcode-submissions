class Solution:
    def isValid(self, s: str) -> bool:
        values = {")" : "(", "]" : "[", "}" : "{"}
        stack = []
        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    if values[char] != stack.pop():
                        return False
        if stack:
            return False
        return True
                
