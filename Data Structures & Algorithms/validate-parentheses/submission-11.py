class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {']':'[', '}':'{', ')':'('}
        for bracket in s:
            if bracket in match:
                if not stack: 
                    return False
                if stack.pop() != match[bracket]:
                    return False
            else:
                stack.append(bracket)
        return not stack