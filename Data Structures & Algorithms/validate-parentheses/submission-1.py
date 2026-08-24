class Solution:
    def isValid(self, s: str) -> bool:
    
        ans = True
        strList = []

        for i in s :
            strList.append(i)
        
        dick = {
            '(' : ')',
            '[':']',
            '{':'}'
        }

        stack = []

        for char in strList:
            if char in dick:
                stack.append(char)
            elif char in dick.values():
                if not stack or dick[stack.pop()] != char:
                    ans = False
                    break

        if len(stack) != 0:
            ans = False
        
        return ans
