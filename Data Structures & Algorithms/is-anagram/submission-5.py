class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sCount = []
        tCount = []

        for char in s.lower():
            sCount.append(char) 

        for char in t.lower():
            tCount.append(char)

        sCount.sort()
        tCount.sort()


        ans = False
        if sCount == tCount :
            ans = True

        return ans
        