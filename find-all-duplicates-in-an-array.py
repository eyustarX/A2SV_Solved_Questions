from collections import Counter

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        num=Counter(nums)
        
        return [n for n in num if num[n]==2]
