class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {']':'[', '}':'{', ')':'('}
        for bracket in s:
            if bracket in match and stack:
                if stack.pop() != match[bracket]:
                    return False
            else:
                stack.append(bracket)
        return not stack