class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        #ctr = 0
        for i in range(len(nums)):
            cur =  nums [i]
            for j in range(i + 1, len(nums)):
                #ans = []
                toCheck = cur + nums[j]
                if target == toCheck:
                    ans.append(i)
                    ans.append(j)
        return ans
        