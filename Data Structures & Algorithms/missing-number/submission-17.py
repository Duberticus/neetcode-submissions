class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        fullList = []
        while n >= 0 :
            fullList.append(n)
            n = n-1

        dif = (set(fullList)-set(nums))

        ldif = list(dif)
        ans = ldif[0]

        return ans