class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = {}
        def toCalc(n):
            if n == 0:
                return 1
            if n < 0:
                return 0
            if n in memo:
                return memo[n]

            ans = toCalc(n - 1) + toCalc(n - 2)
            memo[n] = ans
            return ans

        return toCalc(n)