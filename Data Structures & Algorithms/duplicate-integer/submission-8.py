class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        toCMP = set()

        for i in nums:
            if i in toCMP:
                return True
            toCMP.add(i)
        return False