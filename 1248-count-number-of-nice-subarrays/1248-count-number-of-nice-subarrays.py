class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(k):
            count = left = ans = 0

            for right in range(len(nums)):
                if nums[right] % 2 == 1:
                    count += 1
                
                while count > k:
                    if nums[left] % 2 == 1:
                        count -= 1
                    left += 1
                ans += right - left + 1
            return ans            
        
        return atMost(k) - atMost(k-1)