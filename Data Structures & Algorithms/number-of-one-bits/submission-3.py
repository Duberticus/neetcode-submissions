class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)[2:]
        bitLis = []

        for char in n:
            bitLis.append(int(char))
        ctr = 0
        for idx,i in enumerate(bitLis):
            if i == 1:
                ctr = ctr +1
        return ctr
