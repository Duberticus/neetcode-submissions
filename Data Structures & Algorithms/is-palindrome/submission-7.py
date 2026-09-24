import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        #cleaned = re.sub(r' ', '', s)

        cleaned_text = "".join(char for char in s if char.isalnum())


        liss = []

        for c in cleaned_text:
            liss.append(c)

        i = 0
        j = (len(liss) -1)

        while i<=j:
            
            if liss[j] != liss[i]:
                return False

            i=i+1
            j = j-1
        return True

