class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        j = max(nums)
        nums = set(nums)

        for k in range(1, j + 1):
            if k not in nums and k > 0:
                return k

        return j + 1 if j + 1 > 0 else 1