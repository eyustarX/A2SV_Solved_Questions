class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix=0
        count=0
        freq={0:1}
        
        for i in range(len(nums)):
            prefix+=nums[i]

            if prefix-k in freq:
                count += freq[prefix-k]

            freq[prefix] = freq.get(prefix,0)+1

        return count