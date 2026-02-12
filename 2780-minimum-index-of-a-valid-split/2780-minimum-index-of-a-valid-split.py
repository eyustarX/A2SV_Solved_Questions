class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        freq = Counter(nums)
        dominant, count = freq.most_common(1)[0]

        occur = 0
        for i in range(len(nums)):
            if nums[i] == dominant:
                occur += 1
                if occur * 2 > i + 1 and (count - occur) * 2 >len(nums) - i - 1:
                    return i

        return -1 
            