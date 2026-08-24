class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        temp = 0
        arr = []
       #res = int()
        for i in range(len(prices)):
            res = temp
            for j in range(i+1, len(prices)):
                cmp = prices[j] - prices[i]
                if temp < cmp:
                     temp = cmp
            arr.append(temp)
          
        return arr[-1]
            
