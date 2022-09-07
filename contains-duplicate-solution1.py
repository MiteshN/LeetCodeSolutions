class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsD = set(nums)
        if len(numsD) == len(nums):
            return False
        else:
            return True