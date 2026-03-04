class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]

        mini = min(nums)
        start = 1
        while start:
            k = mini + start
            if k > 0:
                return start
            
            start += 1

