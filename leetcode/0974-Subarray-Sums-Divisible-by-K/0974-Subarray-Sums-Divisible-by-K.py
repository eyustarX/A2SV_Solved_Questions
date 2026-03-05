class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        
        freq = {0:1}
        count = 0

        for i in range(len(nums)):
            mod = nums[i] % k
            if mod not in freq:
                freq[mod] = freq.get(mod, 0) + 1
            
            else:
                count += freq[mod]
                freq[mod] += 1
        
        return count