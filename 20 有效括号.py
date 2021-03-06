class Solution:
    def isValid(self, s: str) -> bool:
        temp = []
        if len(s) < 2: return False
        for i in s:
            if i in '({[':
                temp.append(i)
            else:
                if temp == []: return False
                if i == ')':
                    if temp[-1] == '(':
                        temp.pop(len(temp)-1)
                    else:
                        return False
                if i == ']':
                    if temp[-1] == '[':
                        temp.pop(len(temp)-1)
                    else:
                        return False
                if i == '}':
                    if temp[-1] == '{':
                        temp.pop(len(temp)-1)
                    else:
                        return False
        if temp == []:
            return True
        else:
            return False