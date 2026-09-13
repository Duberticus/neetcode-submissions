class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        toCmp = list(set(nums))

        if len(nums) == len(toCmp):
            return False
        else:
            return True


