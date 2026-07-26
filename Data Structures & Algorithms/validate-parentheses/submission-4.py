class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        string = {'{':'}','[':']','(':')'}
        

        for ch in s:
            if ch in '{([':
                stack.append(ch)
            else:
                if not stack:
                    return False
                if string[stack.pop()]!=ch:
                    return False
        return not stack
            