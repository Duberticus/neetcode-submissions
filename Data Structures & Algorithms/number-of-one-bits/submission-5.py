class Solution:
    def hammingWeight(self, n: int) -> int:
        ctr = 0
        while n != 0:
            check = n & 1
            if check == 1:
                ctr = ctr + 1
            n = n >> 1
        return ctr
