class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cpr = set(nums)
        
        if len(cpr) == len(nums):
            return False
        else:
            return True
