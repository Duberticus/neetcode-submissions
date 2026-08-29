class Solution:
    def hammingWeight(self, n: int) -> int:
        ctr = 0
        ans = 0
        while ctr <= 32:
            var = n & 1
            n = n >> 1
            ans = ans + var

            ctr = ctr + 1
        return ans
        