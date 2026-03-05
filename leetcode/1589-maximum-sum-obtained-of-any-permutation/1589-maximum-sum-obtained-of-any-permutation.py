class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        prefix = [0] * len(nums)

        for l, r in requests:
            prefix[l] += 1
            if r + 1 < len(nums):
                prefix[r + 1] -= 1
        
        for i in range(1, len(nums)):
            prefix[i] += prefix[i - 1]

        prefix.sort(reverse=True)
        nums.sort(reverse=True)

        ans = 0

        for i, j in zip(prefix, nums):
            ans = (ans + i * j) % mod
        
        return ans