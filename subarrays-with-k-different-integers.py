class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atmostK(k):
            count = 0
            hash_map = defaultdict(int)
            left = 0

            for right in range(len(nums)):
                hash_map[nums[right]] += 1

                while len(hash_map) > k:
                    hash_map[nums[left]] -= 1
                    if hash_map[nums[left]] == 0:
                        del hash_map[nums[left]]
                    left += 1
                    
                count += right - left + 1

            return count
        
        return atmostK(k) - atmostK(k-1)
