class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ans = False
        s = set(nums)
        if len(s) != len(nums):
            ans = True
    
        return ans