class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num=Counter(nums)
        for key in num:
            if num[key]>1:
                return True
        return False
