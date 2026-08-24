class Solution:
    def countBits(self, n: int) -> List[int]:
 
        def bigDick(n):
            bd = []
            while n > 0 :
                val = n % 2
                bd.insert(0,val)
                n = n // 2

            counter = 0
            for i,k in enumerate(bd):
                if k == 1:
                    counter = counter + 1

            return counter

        def glue(t) :
            ctr = 0
            liszt = []
            while ctr < t+1 :
                toAp = bigDick(ctr)
                liszt.append(toAp)
                ctr = ctr + 1
            return liszt
        return glue(n)