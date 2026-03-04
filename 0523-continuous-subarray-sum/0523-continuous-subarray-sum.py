class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        
        freq = {0:-1}
        for i, num in enumerate(nums):
            value = num % k

            if value not in freq:
                freq[value] = i

            elif value in freq:
                if i - freq[value] >= 2:
                    return True
        print(freq)
        return False