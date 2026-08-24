class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            to_add = nums[i]
            for j in range(i +1, len(nums)):
                sum  = to_add+ nums[j]
                if sum == target:
                    return [i , j]
        return []