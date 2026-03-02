class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = [0] * len(nums)

        for i, num in enumerate(nums):
            runningSum[i] = runningSum[i-1]+num

        return runningSum