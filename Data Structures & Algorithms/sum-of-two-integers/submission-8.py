class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF

        a = a & mask
        b = b & mask

        while b != 0:
            noCarry = (a ^ b) & mask
            toRet = ((a & b) << 1) & mask

            a = noCarry
            b = toRet

        # Convert 32-bit unsigned result back to signed
        if a <= 0x7FFFFFFF:
            return a
        else:
            return a - 0x100000000