class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        for i in s:
            if i == '[' or i == '(' or i == '{':
                arr.append(i)
                continue
            elif len(arr) == 0:
                return False
            if i == ']':
                if arr[-1] == '[':
                    arr.pop()
                else:
                    return False
            elif i == '}':
                if arr[-1] == '{':
                    arr.pop()
                else:
                    return False
            elif i == ')':
                if arr[-1] == '(':
                    arr.pop()
                else:
                    return False
            else:
                return False
        return len(arr) == 0
            
            