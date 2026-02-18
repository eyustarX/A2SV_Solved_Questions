class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        num = sorted(nums)
        for n in nums:
            ans.append(num.index(n))
        
        return ans