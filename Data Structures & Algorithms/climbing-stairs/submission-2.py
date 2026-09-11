class Solution:
    def climbStairs(self, n: int) -> int:
        ulti = 1
        penUlti = 1

        for i in range(n-1):
            temp = penUlti
            penUlti = penUlti + ulti
            ulti = temp
        
        return penUlti
            